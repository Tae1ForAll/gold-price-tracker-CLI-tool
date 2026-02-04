import gprice.gold_price as gold_price
import gprice.data_manager as data_manager
import gprice.model as model
import gprice.utils as utils

def handle(args: model.InputArgs):
    purity = utils.extract_percent_float(args.purity) if args.purity else 100 
    
    data = gold_price.get_gold_price(args.unit_type, args.currency, purity)
    data_manager.save_price(data)
    utils.print_auto(str(data))

