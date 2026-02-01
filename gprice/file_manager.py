from pathlib import Path
import tomli_w
import tomllib

BASE_DIR = Path.home() / ".gprice"
CONFIG_PATH = BASE_DIR / "config.toml"
CREDS_PATH = BASE_DIR / "credentials.toml"
STATE_PATH = BASE_DIR / "state.toml"

# save
def save_config(new_config: dict): _save(CONFIG_PATH, new_config)
def save_credentials(new_creds: dict): _save(CREDS_PATH, new_creds)
def save_prev_price(price: dict): _save(STATE_PATH, price)

# load
def load_config(): return _load(CONFIG_PATH)
def load_creds(): return _load(CREDS_PATH)
def load_state(): return _load(STATE_PATH)

# save/load config file
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
