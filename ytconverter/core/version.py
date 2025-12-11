import httpx

from ytconverter.config import load_local_version
from ytconverter.constants import PYPI_VERSION_URL


def check_version():
    try:
        remote = httpx.get(PYPI_VERSION_URL, timeout=3).json()["info"]["version"]
    except Exception as e:
        print(e)
        exit()
        return None, None
    local_version, version_type = load_local_version()
    return local_version, remote

if __name__ == "__main__":
  print(check_version())
