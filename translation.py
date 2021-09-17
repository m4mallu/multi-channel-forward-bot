class Translation(object):
    START_MSG = "<b>Hello: {}\nI am a Simple Bot that can Forward messages to your Channels</b>"
    HELP = "1️⃣ <b>Select any of the channels from 1 to 5 to set a default channel to forward messages.</b>\n\n" \
           "2️⃣ <b>Replay 👉 /send command to any Telegram media to forward the message to default channel." \
           "</b>\n\n3️⃣  <b>Select command 👉 /view to view the default forwarding channel.</b>\n\n" \
           "4️⃣ <b>Channel1 is mandatory and others are optionals. Configure ENV carefully for the smooth working." \
           "</b>\n\n5️⃣ <b>You can see my repo [Here](https://github.com/m4mallu/multi-channel-forward-bot)</b>\n\n" \
           "<b>For any suggestions and feedbacks, feel free to contact my developer [Here](" \
           "https://t.me/space4renjith)</b> "
    SUCCESSFUL_SEND = "<code>Forwarded Successfully to:</code>\n<b>{}</b>"
    FORWARD_ERROR = "<code>Make Sure That I am Admin in Your Channel or Provided Channel ID is Correct.</code>"
    CHANNEL_CONFIRM = "<code>Now I'll forward messages to:</code>\n👉 <b>{}</b>"
    INVALID_CHANNEL = "⚠️ <b>Attention :</b>\n<code>Invalid Channel Id Selected.\nPossible Causes of this " \
                      "error:</code>\n\n1️⃣ <b>Bot is not an admin in Your Channel</b>\n\n2️⃣ <b>You haven't entered "\
                      "a valid channel id in the config ENV.</b>\n\n3️⃣ <b>You haven't set a default channel in the " \
                      "bot for the process.</b> "
    NOT_AUTH_TXT = "⚠️ <b>Unauthorized Access</b> ⚠️\n<code>You are not in Auth Users.  So you can't use the core " \
                   "components of this bot. Inconvenience is regretted !</code> "
    NOT_REPLIED_TO_MESSAGE = "⚠️ <b>Attention :</b>\n<code>Replay to any message to send !</code>"
    NO_SPAM_MSG = "⚠️ <b>Attention : Don't Spam Here</b>\n<code>Read the welcome message for better use of this bot " \
                  "!</code> "
    INFO_CHANNEL = "A'm currently sending messages to:\n<b>{}</b>"
    NO_DEFAULT_SET = "⚠️ <b>Attention :</b>\n<code>No Default channels found! Set a channel first.</code>"
