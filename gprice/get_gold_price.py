import os
import dotenv
dotenv.load_dotenv()

import requests
from . import error
from datetime import datetime
from .model import PriceInfo

# load configs
SOURCE_URL = os.getenv('SOURCE_URL')
USER_AGENT = os.getenv('USER_AGENT')

def get_gold_price(currency: str='USD'):
    target_url = f'{SOURCE_URL}{currency}'
    headers = {'User-Agent': USER_AGENT}
    response = requests.get(target_url, headers=headers)
    
    if response.status_code != 200:
        raise error.APIRequestError(f'API request issue: {response.status_code}')

    # deserialize json
    data: dict =  response.json()['items'][0]    
    gold_price = PriceInfo(
        price=data['xauPrice'], 
        currency=data['curr'],
        current_time=datetime.now()
    )
    return gold_price