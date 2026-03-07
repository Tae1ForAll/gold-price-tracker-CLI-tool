import requests
from datetime import datetime

import gprice.error as error 
import gprice.data_manager as data_manager
import gprice.model as model
import gprice.utils as utils

# mulipliers used to convert from oz to a specific unit of measurement
UNIT_MULTIPLIER = {
    "oz": 1.0000, # default
    "thai_baht": 0.4902,
    "china_tael": 0.8337,
    "hk_tael": 0.8307,
    "taiwan_tael": 0.8294,
    "tola": 2.6667
}

def get_gold_price(
    unit_type: str='oz', 
    currency: str='USD', 
    purity: float = 100.0
    ):
    
    try:
        # validate multiplier key
        if unit_type not in UNIT_MULTIPLIER:
            unit_type = 'oz'
            utils.print_warning("Invalid gold unit type, it's automatically set to troy ounce (oz)")    

        if not currency:
            currency = 'USD'
            
        if not purity:
            purity = 100.0
            
        SOURCE_URL = data_manager.SOURCE_URL
        CONFIG = data_manager.load_config()
        
        target_url = f'{SOURCE_URL}{currency}'
        headers = {
            'User-Agent': CONFIG.header.user_agent,
            "Referer": "https://goldprice.org/",
            "Origin": "https://goldprice.org",
            "Accept": "*/*"
        }
        response = requests.get(target_url, headers=headers)
        
        if response.status_code != 200:
            raise error.APIRequestError(f'API request issue: {response.status_code}')
        
    
        # deserialize json
        data: dict =  response.json()['items'][0]    
        price = data['xauPrice']
        currency = data['curr']
        # convert price to specific unit type and purity percentage
        multiplier = UNIT_MULTIPLIER[unit_type] 
        price_after_conversion = price * multiplier * (purity/100)
        
        gold_price = model.PriceInfo(
            price=price_after_conversion,
            unit_type=unit_type, 
            currency=data['curr'],
            purity_in_percent=purity,
            current_time=datetime.now()
        )
        return gold_price
    
    except error.APIRequestError as e:
        utils.print_auto(str(e))
    except Exception as e:
        utils.print_auto(str(e))
