from .. import model, data_manager
import getpass
import gprice.sender as sender

def handle_set_credential(args: model.InputArgs):
    if args.sender_email is None: 
        return
        
    app_password = getpass.getpass("Enter app password: ")
    
    # create sender info
    sender_email_info = model.SenderEmailInfo(
        email=args.sender_email,
        password=app_password)
    
    # create credential
    credential = model.CredentialInfo(sender_email=sender_email_info)
    
    if sender.check_email_credential(credential):
        data_manager.save_credential(credential)    
    else:
        print("Invalid Email or App password, Please enter again")

def handle_set_config(args: model.InputArgs):
    config_info = data_manager.load_config()
    
    if args.header:
        # header value:
        key, value = parse_kv(args.header)
        match key:
            case "user-agent": config_info.header.user_agent = value
            case __: raise ValueError("no keys matched (Please read the document)")
            
    if args.smtp:
        key, value = parse_kv(args.smtp)
        match key:
            case "server":
                smtp_port = int(input_with_default("Enter SMTP port", 587))
                config_info.smtp.port = smtp_port
                config_info.smtp.server = value
            case __: raise ValueError("no keys matched (Please read the document)")
    
    data_manager.save_config(config_info)
    
def input_with_default(message: str, default):
    x = input(message + f'[{default}]:')
    return x if x else default

def parse_kv(pair: str) -> tuple[str, str]:
    if "=" not in pair:
        raise ValueError("Expected key=value")
    key, value = pair.split("=", 1)
    return key.strip(), value.strip()