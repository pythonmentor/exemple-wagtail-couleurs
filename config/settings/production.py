from .base import *
from .base import env

import pymysql

DEBUG = False

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Configuration de MariaDB
DATABASES = {
    "default": env.db("DATABASE_URL") | {},
}
DATABASES["default"]["OPTIONS"] = {
    "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
}
pymysql.install_as_MySQLdb()

STATIC_ROOT = env("STATIC_ROOT")
MEDIA_ROOT = env("MEDIA_ROOT")

# ... + config de production
