# Multi Channel Forward Bot
A Simple Bot which forwards Messages /media to multiple channels.

### Help

- **Bot need to be an admin of the channel with 'post message' privilege.**
- 5 channels can be added to the bot for forwarding. Channel1 is mandatory while the others are optionals.
- select the required channel to set a default channel by the command ```/channel1```   to    ```/channel5``` .
- Reply to the telegram media with ```/send``` command to forward.
- Give ```/view``` command to view the present default channel selected for forwarding.

### Bot Commands
```
/start - Start Message
/help - Help Message

/send - Send the replied message to the default channel(As a reply to any telegram message)
/view - View the deault channel
/channel1 - Set channel 1 as default forwaring channel (Optional)
/channel2 - Set channel 2 as default forwaring channel (Optional)
/channel3 - Set channel 3 as default forwaring channel (Optional)
/channel4 - Set channel 4 as default forwaring channel (Optional)
/channel5 - Set channel 5 as default forwaring channel (Optional)

```

### Environment Variables

```
TG_BOT_TOKEN - Your Bot Token (Obtain from @botfather)
APP_ID - Your APP ID (Obtain from my.telegram.org)
API_HASH - Your API Hash (Obtain from my.telegram.org)

CHANNEL1_ID - Id of your chnnel (Use any channel Id bots to find it and don't forget to Put a prefix "-100" to the value)
CHANNEL2_ID - Id of your chnnel (Optional)
CHANNEL3_ID - Id of your chnnel (Optional)
CHANNEL4_ID - Id of your chnnel (Optional)
CHANNEL5_ID - Id of your chnnel (Optional)

CHANNEL1_NAME - Name of your channel
CHANNEL2_NAME - Name of your channel (Optional)
CHANNEL3_NAME - Name of your channel (Optional)
CHANNEL4_NAME - Name of your channel (Optional)
CHANNEL5_NAME - Name of your channel (Optional)
```

### Deploying on Heroku (Easy Way):

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/m4mallu/multi-channel-forward-bot)

### On Linux PCs or VPS (Legendary Way):
- Create a ```config.py``` file with the environment variables.
- Finally, run the following

```
virtualenv -p python3 venv
. ./venv/bin/activate
pip3 install -r requirements.txt
python3 bot.py
```

### Developed By:
[Mallu Boy](https://github.com/m4mallu) as [Renjith](https://t.me/space4renjith) on Tg

### Courtesy:
[Adithyan](https://github.com/Adithyan1133-ctrl) for his [Channel Forward Bot](https://github.com/Adithyan1133-ctrl/CHNL-Forward-Bot)

[Dan](https://t.me/huskell) for his [Pyrogram](https://github.com/pyrogram/pyrogram) Library
