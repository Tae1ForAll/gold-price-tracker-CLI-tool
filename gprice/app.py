# extranal module
import argparse

# internal module
import gprice.commands as commands
from gprice import __version__

def main():    
    # set up parsers
    parser = argparse.ArgumentParser(prog='Gold price tracker [CLI Tool]') 
    parser.add_argument('-v', '--version', action="version", version=f"%(prog)s {__version__}")
    parser.add_argument('-i', '--info', action="store_true")

    # setup subparsers
    subparsers = parser.add_subparsers(dest="command")
    get_parser = subparsers.add_parser('get', help="")
    set_cred_parser = subparsers.add_parser('set-credential', help="")
    set_config_parser = subparsers.add_parser('set-config', help="Set config [-h (--header)]")
    noti_parser = subparsers.add_parser('noti', help="")
        
    # setup "get" commands
    get_parser.add_argument('-c', '--currency')
    
    # setup "set" commands *********************************************************************    
    set_cred_parser.add_argument('-sm', '--sender-email', dest='sender_email')
    set_config_parser.add_argument('-header', '--header', 
                                   metavar="key=value", 
                                   help="Set header config (eg. user_agent=value)")
    # ******************************************************************************************

    # setup "noti" (noti notification) commands ************************************************
    noti_parser.add_argument('-eve', '--every', dest="every") # schedule checking gold price
    noti_parser.add_argument('-c', '--currency', dest="currency") # target currency
    noti_parser.add_argument('-to', '--to', dest="recipient") # recipient
    noti_parser.add_argument('-if', '--if_con', nargs="+", default=[])
    #*******************************************************************************************

    commands.run(parser.parse_args())