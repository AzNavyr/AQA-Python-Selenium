import yaml
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "settings.yaml"

with open(CONFIG_PATH, "r") as f:
    settings = yaml.safe_load(f)
