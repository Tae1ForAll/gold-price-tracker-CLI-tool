import requests
from . import error, data_manager
from datetime import datetime
import gprice.model as model

def get_gold_price(currency: str='USD'):
    SOURCE_URL = data_manager.SOURCE_URL
    CONFIG = data_manager.load_config()
    
    target_url = f'{SOURCE_URL}{currency}'
    headers = {'User-Agent': CONFIG.header.user_agent}
    response = requests.get(target_url, headers=headers)
    
    if response.status_code != 200:
        raise error.APIRequestError(f'API request issue: {response.status_code}')

    # deserialize json
    data: dict =  response.json()['items'][0]    
    gold_price = model.PriceInfo(
        price=data['xauPrice'], 
        currency=data['curr'],
        current_time=datetime.now()
    )
    return gold_price