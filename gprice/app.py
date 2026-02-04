# extranal module
import argparse

# internal module
import gprice.commands as commands
from gprice import __version__

def main():    
    # set up parsers
    parser = argparse.ArgumentParser(prog='Gold price tracker [CLI Tool]') 
    parser.add_argument('-v', '--version', action="version", version=f"%(prog)s {__version__}")
    parser.add_argument('-i', '--info', action="store_true", help="Show program infomation such as credentials, configs, and more")

    # setup subparsers
    subparsers = parser.add_subparsers(dest="command")
    get_parser = subparsers.add_parser('get', help="Fetch current gold price")
    set_cred_parser = subparsers.add_parser('set-credential', help="")
    set_config_parser = subparsers.add_parser('set-config', help="Set config such as smtp server, port")
    noti_parser = subparsers.add_parser('noti', help="")
        
    # setup "get" commands
    get_parser.add_argument('-c', '--currency', 
                            metavar="",
                            help="determines gold price currency default, USD")
    
    get_parser.add_argument('-p', '--purity', 
                            metavar="",
                            help="determines purity of gold default 100")
    
    get_parser.add_argument('-u', '--unit_type', 
                            metavar="",
                            help="determines a specific weight unit such as taiwan_tael, thai_baht")
    
    # setup "set" commands *********************************************************************    
    set_cred_parser.add_argument('-sm', '--sender_email', metavar="")
    set_config_parser.add_argument('--header', 
                                   metavar="", 
                                   help="Set header config > keys: user_agent (eg. user_agent=value) \n ")
    set_config_parser.add_argument('-smtp', 
                                   metavar="",
                                   help="Set SMTP values > key: server (eg. server=smtp.gmail.com)")
    # ******************************************************************************************

    # setup "noti" (noti notification) commands ************************************************
    noti_parser.add_argument('-eve', '--every') # schedule checking gold price
    noti_parser.add_argument('-c', '--currency') # target currency
    noti_parser.add_argument('-to', '--to', dest="recipient") # recipient
    noti_parser.add_argument('-if', '--if_con', nargs="+", default=[])
    #*******************************************************************************************

    commands.run(parser.parse_args())