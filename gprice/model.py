from dataclasses import dataclass
import datetime

@dataclass
class InputArgs:
    command: str
    info: bool
    
    # options
    currency: str | None
    purity: str
    unit_type: str
    
    # parsers for set-credential
    sender_email: str | None
    
    # parsers for set-config
    header: str | None
    smtp: str | None
    
    # parsers for noti commands
    every: str
    recipient: str
    if_con: list[str]

# convert_price
@dataclass
class PriceInfo:
    price: float
    currency: str
    unit_type: str 
    purity_in_percent: float 
    current_time: datetime
    
    def __str__(self):
        unit_type = self.unit_type.replace('_', ' ')
        
        return f'''
            gold price    : {self.price} {self.currency}
            weight unit   : {unit_type}
            purity (%)    : {self.purity_in_percent}%
            requested at  : {self.current_time}
        '''        

# credential ================================
@dataclass
class SenderEmailInfo:
    email: str
    password: str
        
@dataclass
class CredentialInfo:
    sender_email: SenderEmailInfo
# ===========================================

# configs ===================================
@dataclass
class SMTPInfo:
    server: str
    port: int
    
@dataclass
class HeaderInfo:
    user_agent: str
    
@dataclass
class ConfigInfo:
    header: HeaderInfo
    smtp: SMTPInfo
# ===========================================