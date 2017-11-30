# PTT Notifier
This is a lightweight PTT notifier which helps you monitor posts with keywords you interested in. For example, if you are looking for a Nvidia 1080 Ti on HardwareSell board, you can set keywords '1080', '賣' and make the notifier monitor the HardwareSell board. Once there is a post that is selling the GPU card, the notifier will notify you through telegram immediately.

## Installation
This project uses python3, some python packages and SQLite, make sure SQLite is installed in your system. Just install the required python packages through:

    sudo -H pip3 install -r requirements.txt
    
.

After that, you need to register a [telegram](https://telegram.org) account, and [create a telegram bot](https://core.telegram.org/bots) through the bot father.

## Configuration
All the configurations are set in the `configure.py` file, and you can copy a configuration file from `configure.py.example`.

### telegram_config
After copy and rename the configuration file, the first thing you need to configure is your `bot_key`, you can get this key through bot father when the bot is created, or request this key later via bot father with the command conservation.

There is a `notified_chat_ids` in `telegram_config`, this field allows you to decide which chats can get notifications (note: to send notifications to group chat, you need to manually add the bot to that group first). Actually people don't know their chat id, you can get some help from `easy_get_chat_id.py`. Just send the bot a text message, and execute this script

    python3 easy_get_chat_id.py
    
The script will tell you the chat id where the bot got the last message.

### ptt_config
You can configure some parameters here:

* monitor\_interval: the unit is second, which indicates how long the bot will sleep every time the bot request posts from ptt. Remember, do not request too frequently or the ptt will reject your request.
* checked\_posts\_db: I use SQLite to store the posts already seen. Give the SQLite db file a name, and the bot will generate a .db file. Do not delete the .db file, or your bot will forget posts already seen.
* monitor\_boards: the boards you want to monitor.

### filter_config
You can configure the keywords you are interested in.

* required_keywords: the post must match all keywords in this field, if you set case sensitive to false, enter the lower case English keywords.
* optional_keywords: the post must match at least one keywords in the field. If you leave this field empty, then this configuration does not work.

## Monitoring
Once you complete the configuration, you can start to run the ptt notifier!

    python3 notifier.py
