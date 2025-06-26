from os import getenv

workers = getenv("GUNICORN_WORKERS", "2")

bind = "0.0.0.0:" + getenv("APP_PORT", "8000")
