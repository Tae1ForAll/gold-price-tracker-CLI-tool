from .. import scheduler, sender, model 
from ..condition_parser import Direction, Condition, parse_conditions
import gprice.gold_price as gold_price
import gprice.data_manager as data_manager

def handle_noti(args: model.InputArgs):   
    # set up job
    def job():
        if args.recipient == None:
            return
        
        # load gold prices
        old_data = data_manager.load_prev_price()
        new_data: model.PriceInfo = gold_price.get_gold_price(args.currency)        
        
        # check if the new price matches the conditions or not
        is_noti = True
        if args.if_con and old_data:
            cons = parse_conditions(args.if_con)
            diff = new_data.price - old_data.price
            is_noti = check_condition(diff, cons)
        
        # send notification
        if is_noti:
            body = f'''
                current  price: {new_data.price} ({new_data.currency}/oz)
                previous price: {str(old_data.price) + f' ({old_data.currency}/oz)' if old_data else "Unknown"}
                requested at  : {new_data.current_time}
            '''
            
            subject = "Current Gold Price"
            if old_data:    
                if new_data.price > old_data.price: subject="Price goes up!!"  
                elif new_data.price < old_data.price: subject="Price goes down!!"
                else: subject="Price remain the same"
            
            sender.send_email_notification(body=body, subject=subject, receiver_email=args.recipient)   
            data_manager.save_price(new_data)
        
    if args.every:         
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