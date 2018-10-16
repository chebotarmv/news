# -*- coding: utf-8 -*-
from app import app
import requests
from flask import render_template



@app.route('/')
@app.route('/index')
def index():
    posts = []
    new_article = requests.get('https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty')
    article_list = new_article.json()[:20]
    for article in article_list:
        data = requests.get('https://hacker-news.firebaseio.com/v0/item/' + str(article) + '.json?print=pretty')
        if 'url' in data.json():
            context = {}
            context['url'] = data.json()['url']
            context['title'] = data.json()['title']
            posts.append(context)
    return render_template('index.html', posts=posts)