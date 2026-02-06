from .. import data_manager

def handle_info():
    print("\n")
    _display_configures()
    print("\n")    
    _display_credentials()
    print("\n")    
        
# internals
def _display_configures():
    cfg = data_manager.load_config()
    
    # Header
    print("Config:")
    print("  Header")
    print(f"    User-Agent:     {cfg.header.user_agent}")

    # smtp
    print("  SMTP Infomation")
    print(f"    SMTP server:    {cfg.smtp.server}")
    print(f"    SMTP port:      {cfg.smtp.port}")

    #==================================================================
    
def _display_credentials():
    path = data_manager.CREDS_PATH
    
    if not path.exists():
        print("Credentials not yet initialized.")
        return
    
    print(f"Credentials")
    creds = data_manager.load_credential()
    
    # display sender email
    if creds.sender_email:
        print("  Sender Email")
        print(f"    Email:          {creds.sender_email.email}")
        print(f"    App password:   {"*********" if creds.sender_email.password else "(not set)"}\n")
    else:
        print("  Sender Email: (not yet initialized)")    
    