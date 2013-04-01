# -*- coding: utf-8 -*-

import requests

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/content/<uuid>')
def get_content(uuid):
    pass

# TODO: .rss?
@app.route('/<collection>.atom')
def get_collection_feed(collection):
    pass

@app.route('/<collection>/<category>.atom')
def get_category_feed(collection, category):
    pass



if __name__ == '__main__':
    app.run()