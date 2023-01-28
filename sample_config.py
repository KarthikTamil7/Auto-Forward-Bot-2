import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5949999646:AAGNAzsUTMutsqtnSk2R4MkGgCQ0uMtqbIU")
    APP_ID = int(os.environ.get("APP_ID", 11973721))
    API_HASH = os.environ.get("API_HASH", "5264bf4663e9159565603522f58d3c18")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001342411240:-1001518309911"))
