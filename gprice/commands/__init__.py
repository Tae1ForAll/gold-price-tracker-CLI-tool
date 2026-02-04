# external
from .info_handler import handle_info
from .noti_handler import handle
from .set_handler import handle_set_config, handle_set_credential
from .get_handler import handle
import gprice.model as model

def run(args: model.InputArgs):
    match args.command:
        case "set-credential": handle_set_credential(args)
        case "set-config": handle_set_config(args)
        case "get": handle(args)
        case "noti": handle(args)
        case __:
            if args.info: handle_info()