from importlib import import_module
from pathlib import Path
import sys

from config import BASE_DIR

sys.path.insert(0, str(BASE_DIR))

wsgi = import_module("config.wsgi")
application = wsgi.application
