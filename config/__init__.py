import pathlib
import sys

import environ

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config"
PROJECT_DIR = BASE_DIR / "example"

sys.path.insert(0, str(BASE_DIR))

env = environ.Env()
env.read_env(str(BASE_DIR / ".env"))
