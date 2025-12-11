import re

URL_RE = re.compile(r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$")
VERSION_URL = "https://raw.githubusercontent.com/kaifcodec/ytconverter/main/version.json"
PYPI_VERSION_URL = "https://pypi.org/pypi/ytconverter/json"
