from pathlib import Path
import os
import yaml

def _project_root() -> Path:
    """
    return the root dir of the project
    eg:
        if this file loacted at: 
            E:\Project\Medical_Chatbot\chatbot\utils\config_loader.py
        this function return
            E:\Project\Medical_Chatbot
    """
    return Path(__file__).resolve().parents[2]

def load_config(config_path: str | None = None) -> dict:
    """
    loads a YAML configuration file.
    1. if `config_path` is passed use it.
    2. otherwise, if `CONFIG_PATH` env variable exists, use that.
    3. ptherwise, fall back to the default project config file:
        <project_root>/chatbot/config/config.yaml

    return:
        dict: configuration dict parsed from YAML
    """


    # Try to get config path from argument or environment variable
    env_path = os.getenv("CONFIG_PATH") # env

    # if there is not env_path
    if config_path is None: # argument
        config_path = env_path or str(_project_root() / "chatbot"/ "config" / "config.yaml")

    # If the path is relative, make it absolute relative to the project root
    path = Path(config_path)    
    if not path.is_absolute():
        path = _project_root() / path

    # check if fiel exists
    if not path.exists():
        raise FileExistsError(f"config file not found: {path}")
    
    # load YAML file safely
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


