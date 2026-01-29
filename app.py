import argparse
import requests
from set_handler import set_handler, schedule_handler
from datetime import datetime
import os
import dotenv
dotenv.load_dotenv()

import sender
from model import InputArgs, PriceInfo

# custom errors
class APIRequestError(Exception): pass
# =======================================


# load configs
SOURCE_URL = os.getenv('SOURCE_URL')
USER_AGENT = os.getenv('USER_AGENT')

def get_gold_price(currency: str='USD'):
    target_url = f'{SOURCE_URL}{currency}'
    headers = {'User-Agent': USER_AGENT}
    response = requests.get(target_url, headers=headers)
    
    if response.status_code != 200:
        raise APIRequestError(f'API request issue: {response.status_code}')

    # deserialize json
    data: dict =  response.json()['items'][0]    
    gold_price = PriceInfo(
        price=data['xauPrice'], 
        currency=data['curr'],
        current_time=datetime.now()
    )
    return gold_price


def main():
    # set up parsers
    parser = argparse.ArgumentParser(prog='Gold price tracker [CLI Tool]') 

    # setup subparsers
    subparsers = parser.add_subparsers(dest="command")
    set_parser = subparsers.add_parser('set', help="")
    show_parser = subparsers.add_parser('show')
    noti_parser = subparsers.add_parser('noti')
    
    # setup "set" commands
    set_parser.add_argument('-ug', '--user-agent', dest='user_agent')
    set_parser.add_argument('-sm', '--sender-email', dest='sender_email')

    # setup "get" commands
    show_parser.add_argument('-c', '--currency', dest="currency")

    # setup "noti" (noti notification) commands
    noti_parser.add_argument('-eve', '--every', dest="every")
    noti_parser.add_argument('-c', '--currency', dest="currency")
    noti_parser.add_argument('-to', '--to', dest="recipient")
    

    args: InputArgs = parser.parse_args()
        
    if args.command == "set": set_handler(args)    
    elif args.command == "show": print(get_gold_price(args.currency))
    elif args.command == "noti":         
        if args.every: schedule_handler(args)
        else:
            if args.recipient == None:
                return
            gold_price = get_gold_price(args.currency)
    
            # set up body
            body = f'''{str(gold_price)}'''
            sender.send_email_notification(body=body, subject='notification gold tracker', receiver_email=args.recipient)   
    


if __name__ == "__main__":
    main()    