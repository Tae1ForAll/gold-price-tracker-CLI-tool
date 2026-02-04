import gprice.gold_price as gold_price
import gprice.model as model
import gprice.data_manager as data_manager

def handle_get(args: model.InputArgs):
    data = gold_price.get_gold_price(args.currency)
    data_manager.save_price(data)
    print(data)