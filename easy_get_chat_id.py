from config import telegram_config
import requests
import json

res = requests.get('{}{}/getUpdates'.format(telegram_config['base_url'], telegram_config['bot_key']), params={ 'limit': 1 })
result = json.loads(res.text)['result'][0]
print('last message is from chat id: {}'.format(result['message']['chat']['id']))
