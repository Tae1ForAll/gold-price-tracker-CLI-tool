from . import model
from dataclasses import asdict
from pathlib import Path
import tomli_w
import tomllib
from dataclasses import replace

'''
for loading, saving, and caching data
'''

# default config *********************************************
DEFAULT_HEADER = model.HeaderInfo(
    user_agent="curl/8.5.0",    
)
DEFAULT_SMTP = model.SMTPInfo(
    server="smtp.gmail.com",
    port=587
)
DEFAULT_CONFIG = model.ConfigInfo(
    header=DEFAULT_HEADER,
    smtp=DEFAULT_SMTP
)
SOURCE_URL = "https://data-asg.goldprice.org/dbXRates/"
# ************************************************************

BASE_DIR = Path.home() / ".gprice"
CONFIG_PATH = BASE_DIR / "config.toml" # custom config
CREDS_PATH = BASE_DIR / "credentials.toml"
PREV_PRICE_PATH = BASE_DIR / "prev_price.toml"

# save data section *************************************************************************************
def save_credential(new_credential: model.CredentialInfo): _save(CREDS_PATH, asdict(new_credential))
def save_config(new_config: model.ConfigInfo): _save(CONFIG_PATH, asdict(new_config))
def save_prev_price(price: model.PriceInfo): _save(PREV_PRICE_PATH, asdict(price))
# *******************************************************************************************************

# load data section *************************************************************************************
def load_credential():
    data = _load(CREDS_PATH) or {}
    sender_email_data = data.get("sender_email", {})  # dict
    sender_email = model.SenderEmailInfo(**sender_email_data)
    return model.CredentialInfo(sender_email=sender_email)
    
def load_config() -> model.ConfigInfo:
    data = _load(CONFIG_PATH) or {}

    header_data = data.get("header")
    smtp_data = data.get("smtp")

    header = (
        model.HeaderInfo(**header_data)
        if isinstance(header_data, dict)
        else replace(DEFAULT_HEADER)
    )

    smtp = (
        model.SMTPInfo(**smtp_data)
        if isinstance(smtp_data, dict)
        else replace(DEFAULT_SMTP)
    )

    return model.ConfigInfo(
        header=header,
        smtp=smtp,
    )

def load_prev_price() -> model.PriceInfo:
    price_state_dict = _load(PREV_PRICE_PATH)
    return model.PriceInfo(**price_state_dict)
# *******************************************************************************************************


# internals save/load file -----------------------------------------------------------------------------
def _save(path: Path, data: dict):
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("wb") as f:
            tomli_w.dump(data, f)
    except Exception as e:
        raise RuntimeError(f"Failed to save file [path={path}, data={data}]") from e

def _load(path: Path):
    if not path.exists():
        return {}
    
    try:
        text = path.read_text(encoding="utf-8")
        return tomllib.loads(text)
    except Exception as e:
        raise RuntimeError(f"Failed to read file [path={path}]")
# ------------------------------------------------------------------------------------------------------