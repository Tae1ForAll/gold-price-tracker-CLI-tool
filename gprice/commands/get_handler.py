import gprice.gold_price as gold_price
import gprice.model as model

def handle_get(args: model.InputArgs):
    print(gold_price.get_gold_price(args.currency))