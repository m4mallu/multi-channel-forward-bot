import os
import pyrogram

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config

channel = {}
channel_name = {}

if __name__ == "__main__":
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "tg-channel-forward-robot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=300
    )
    app.run()
