import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
    APP_ID = int(os.environ.get("APP_ID"))
    API_HASH = os.environ.get("API_HASH")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    CHANNEL1_ID = os.environ.get("CHANNEL1_ID")
    CHANNEL1_NAME = os.environ.get("CHANNEL1_NAME")
    CHANNEL2_ID = os.environ.get("CHANNEL2_ID")
    CHANNEL2_NAME = os.environ.get("CHANNEL2_NAME")
    CHANNEL3_ID = os.environ.get("CHANNEL3_ID")
    CHANNEL3_NAME = os.environ.get("CHANNEL3_NAME")
    CHANNEL4_ID = os.environ.get("CHANNEL4_ID")
    CHANNEL4_NAME = os.environ.get("CHANNEL4_NAME")
    CHANNEL5_ID = os.environ.get("CHANNEL5_ID")
    CHANNEL5_NAME = os.environ.get("CHANNEL5_NAME")
