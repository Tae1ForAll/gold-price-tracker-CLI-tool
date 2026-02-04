# custom print functions =====================================================
RESET = '\033[0m' # called to return to standard terminal text color
def print_error(message: str):
    RED = '\033[1;38;5;9;49m'
    print(RED + '[ERROR]: ' + message + RESET)

def print_warning(message: str):
    YELLOW = '\033[1;38;5;215;49m' # orange on some systems
    print(YELLOW + '[WARNING]: ' + message + RESET)
    
def print_auto(message: str):
    '''
    for announce an operation status
    '''
    BLUE = '\033[1;38;5;80;49m'
    print(BLUE + '[AUTO]: ' + message + RESET)
# ============================================================================

