from config import ptt_config, telegram_config
import logging
import database
import requests
import time
import crawler

def notify(post):
    text = '新文章: {}, {}'.format(post.title, ptt_config['base_url'] + post.url)
    url = '{}{}/sendMessage'.format(telegram_config['base_url'], telegram_config['bot_key'])
    for chat_id in telegram_config['notified_chat_ids']:
        params = {
            'chat_id': chat_id,
            'text': text
        }
        requests.get(url, params=params)

urls = [ '{}/bbs/{}/index.html'.format(ptt_config['base_url'], board) for board in ptt_config['monitor_boards'] ]

while True:
    posts = []
    for url in urls:
        posts +=  crawler.get_matched_posts(url)
    for post in posts:
        try:
            post_obj = database.Post.create(**post)
            notify(post_obj)
        except:
            logging.info('Post already exists')
    time.sleep(ptt_config['monitor_interval'])
