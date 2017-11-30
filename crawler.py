from bs4 import BeautifulSoup
from config import ptt_config, filter_config
import requests
import re

def parse_post(post_tag):
    return {
        'url': post_tag.attrs['href'],
        'title': post_tag.contents[0] if filter_config['case_sensitive'] else post_tag.contents[0].lower()
    }

def post_filter(post):
    if len(filter_config['required_keywords']) != 0 and not all([ re.search(keyword, post['title']) for keyword in filter_config['required_keywords'] ]):
        return False
    if len(filter_config['optional_keywords']) != 0 and not any([ re.search(keyword, post['title']) for keyword in filter_config['optional_keywords'] ]):
        return False
    return True

def get_matched_posts(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html5lib')
    posts = [ parse_post(post) for post in soup.select('#main-container .bbs-screen .title a') ]
    return list(filter(lambda post: post_filter(post), posts))
