import json
import os
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
VERSION_FILE = _SCRIPT_DIR / "version.json"




def load_local_version():
    try:
        return json.loads(VERSION_FILE.read_text()).get("version"), json.loads(VERSION_FILE.read_text()).get("version_type")
    except Exception:
        return None

