from .model import InputArgs, PriceInfo, SenderEmailInfo
from .get_gold_price import get_gold_price
from .condition_parser import Direction, Condition, parse_conditions
from . import sender
from . import file_manager
from . import scheduler

from typing import Optional
import getpass

def set_handler(args: InputArgs):
    if args.sender_email == None and args.user_agent == None:
        print("input 'gprice set -h' to how to use")
        
    if args.sender_email:
        print("implement set sender-email")
        
        # ask for password then init dataclass with the variables 
        app_password = getpass.getpass("Enter app password")
        info = SenderEmailInfo(email=args.sender_email, password=app_password)
        
        # save config
        info_dict = info.to_dict()
        file_manager.save_credentials(info_dict)
    
    if args.user_agent:
        file_manager.save_config({'user-agent': args.user_agent})

#region "noti" command handler
def noti_handler(args: InputArgs):
    prev_gold_price: Optional[PriceInfo] = None
    
    # set up job
    def job():
        nonlocal prev_gold_price
        
        if args.recipient == None:
            return
        gold_price: PriceInfo = get_gold_price(args.currency)
        
        # check if the new price matches the conditions or not
        is_noti = True
        if args.if_con and prev_gold_price:
            cons = parse_conditions(args.if_con)
            diff = gold_price.price - prev_gold_price.price
            is_noti = check_condition(diff, cons)
        
        # send notification
        if is_noti:
            body = f'''
                current  price: {gold_price.price} ({gold_price.currency}/oz)
                previous price: {str(prev_gold_price.price) + f' ({prev_gold_price.currency}/oz)' if prev_gold_price else "Unknown"}
                requested at  : {gold_price.current_time}
            '''
            
            subject = "Current Gold Price"
            if prev_gold_price:    
                if gold_price.price > prev_gold_price.price: subject="Price goes up!!"  
                elif gold_price.price < prev_gold_price.price: subject="Price goes down!!"
                else: subject="Price remain the same"
            
            sender.send_email_notification(body=body, subject=subject, receiver_email=args.recipient)   
            prev_gold_price = gold_price
    
    if args.every:        
        print(f'Condition : {args.if_con if args.if_con else "Nothing"}')    
        scheduler.run_schedule(args.every, job)
    else: 
        job()

def check_condition(diff: float, cons: list[Condition]) -> bool:        
    for con in cons:
        if con.direction is Direction.UP and diff >= con.amount:
            return True        
        if con.direction is Direction.DOWN and (-diff) >= con.amount:
            return True

    return False

# endregion