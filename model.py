from dataclasses import dataclass
import datetime

@dataclass
class InputArgs:
    command: str
    
    # set commands
    user_agent: str | None
    sender_email: str | None
    
    # schedule commands
    every: str
    
    config: str
    recipient: str
    currency: str
    if_con: list[str]

@dataclass
class PriceInfo:
    price: float
    currency: str
    current_time: datetime
    
    def __str__(self):
        return f'''
            gold price    : {self.price}{self.currency}/oz
            requested at  : {self.current_time}
        ''' 
    
