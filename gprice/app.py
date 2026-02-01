# extranal module
import argparse

# internal module
from .commands import set_handler, noti_handler
from .model import InputArgs
from .get_gold_price import get_gold_price
from gprice import __version__

def main():
    # TODO implement load data
    
    # set up parsers
    parser = argparse.ArgumentParser(prog='Gold price tracker [CLI Tool]') 
    parser.add_argument('-c', '--currency', dest="currency")
    parser.add_argument('-v', '--version', action="version", version=f"%(prog)s {__version__}")


    # setup subparsers
    subparsers = parser.add_subparsers(dest="command")
    get_parser = subparsers.add_parser('get', help="")
    set_parser = subparsers.add_parser('set', help="")
    noti_parser = subparsers.add_parser('noti', help="")
        
    # setup "get" commands
    get_parser.add_argument('-c', '--currency')
    
    # setup "set" commands
    set_parser.add_argument('-ug', '--user-agent', dest='user_agent')
    set_parser.add_argument('-sm', '--sender-email', dest='sender_email')

    # setup "noti" (noti notification) commands
    noti_parser.add_argument('-eve', '--every', dest="every") # schedule checking gold price
    noti_parser.add_argument('-c', '--currency', dest="currency") # target currency
    noti_parser.add_argument('-to', '--to', dest="recipient") # recipient
    noti_parser.add_argument('-if', '--if_con', nargs="+", default=[])

    args: InputArgs = parser.parse_args()
        
    if args.command == "set": set_handler(args)    
    elif args.command == "noti": noti_handler(args)
    else:
        if args.command == "version": 
            print("version")
        # handle main command argument   
        print(get_gold_price(args.currency))