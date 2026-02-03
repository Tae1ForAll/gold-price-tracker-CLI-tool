from .. import scheduler, sender, model 
from ..gold_price import get_gold_price
from ..condition_parser import Direction, Condition, parse_conditions
from typing import Optional

def handle_noti(args: model.InputArgs):
    prev_gold_price: Optional[model.PriceInfo] = None
    
    # set up job
    def job():
        nonlocal prev_gold_price
        
        if args.recipient == None:
            return
        gold_price: model.PriceInfo = get_gold_price(args.currency)
        
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