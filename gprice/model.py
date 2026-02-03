from dataclasses import dataclass
import datetime

@dataclass
class InputArgs:
    command: str
    info: bool
    
    # parsers for set-credential
    sender_email: str | None
    
    # parsers for set-config
    header: str | None
    smtp: str | None
    
    # parsers for noti commands
    every: str
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