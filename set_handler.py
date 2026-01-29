from model import InputArgs
import schedule

def set_handler(args: InputArgs):
    if args.sender_email == None and args.user_agent == None:
        print("input 'gprice set -h' to how to use")
        
    if args.sender_email:
        print("implement set sender-email")
    
    if args.user_agent:
        print("implement setting user-agent")
        
    
def schedule_handler(args: InputArgs):
    pass        