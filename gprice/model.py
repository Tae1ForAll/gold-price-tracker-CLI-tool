from dataclasses import dataclass, asdict
import datetime

@dataclass
class InputArgs:
    command: str
    
    # main parsers
    
    
    # parsers for set commands
    user_agent: str | None
    sender_email: str | None
    
    # parsers for noti commands
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

@dataclass
class SenderEmailInfo:
    email: str
    password: str        
    
    def to_dict(self) -> dict:
        return {"sender-email": asdict(self)}