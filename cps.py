# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, make_response, Response, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy

import settings

app = Flask(__name__)

## Setup SQLAlchemy
## For a relative file path: 3 slashes,  e.g., sqlite:///test.db
## For an absolute file path: 4 slashes, e.g., sqlite:////tmp/test.db
## ref. http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html#sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

######################## test data ########################
articles = []
article1 = {
    "id":1,
    "image_url": u"images/iPhone6.png", 

    "title_zh": u"iPhone 6: 豈止於大", 
    "content_zh": u"<div>新手機上市</div>", 
    "description_zh": u"不只外型變大，更在各方面都顯著提升",

    "title_en": u"iPhone 6: Bigger than bigger", 
    "content_en": u"<div>Latest iphone</div>", 
    "description_en": u"iPhone 6 isn’t simply bigger - it’s better in every way, iPhone 6 isn’t simply bigger - it’s better in every way, iPhone 6 isn’t simply bigger - it’s better in every way"
}

article2 = {
    "id":2,
    "image_url": u"images/samsung_note4.png", 

    "title_zh": u"Samsung Note 4",
    "content_zh": u"<div>新手機上市</div>", 
    "description_zh": u"感應快捷環（Action Memo快捷Memo、Smart Select全能貼、Image Clip全能剪、Screen Write快速截圖）S Note、Snap Note快拍筆記、Direct Pen Input感應筆寫框",

    "title_en": u"Samsung Note 4", 
    "content_en": u"<div>Latest Note</div>", 
    "description_en": u"The precise color saturation and the high contrast of 5.7' Quad HD Super AMOLED display will drive you to feel the fluent and vivid color as if you are looking with the naked eye. High resolution boasts tremendous viewing experience. Truly optimized for web-browsing and e-booking."
}
articles.append(article1)
articles.append(article2)
########################################################################
######################## test data ########################
products = []
product1 = {
    "id":1,
    "image_url": u"images/iPhone6.png", 

    "brand": u"蘋果",

    "title_zh": u"Apple iPhone 6", 
    "content_zh": [u"64G 儲存空間", u"A8 晶片"],
    "html_zh": u"<li>64G 儲存空間</li><li>A8 晶片</li>",
    "type_zh": u"手機",

    "title_en": u"Apple iPhone 6", 

    "content_en": [u"64G Flash", u"A8 Chip"],
    "html_en": u"<li>64G Flash</li><li>A8 Chip</li>",

    "type_en": u"cellphone",
}

product2 = {
    "id":2,
    "image_url": u"images/samsung_note4.png", 

    "brand": u"三星",

    "title_zh": u"Samsung Note 4",
    "content_zh": [u"64G 空間", u"Intel 處理器"],
    "html_zh": u"<li>64G 空間</li><li>Intel 處理器</li>",
    "type_zh": u"手機",

    "title_en": u"Samsung Note 4", 

    "content_en": [u"64G Flash", u"Intel chip"], 
    "html_en": u"<li>64G Flash</li><li>Intel chip</li>", 

    "type_en": u"cellphone",
}
products.append(product1)
products.append(product2)
########################################################################


###############################
##         Locations         ##
###############################

@app.route('/')
@app.route('/<lang>')
@app.route('/<lang>/')
def index(lang=settings.LANG):
    return render_template( 'index.tpl', settings=settings, lang=lang )

@app.route('/<lang>/news')
@app.route('/<lang>/news/')
@app.route('/<lang>/news/list')
@app.route('/<lang>/news/list/')
def show_news(lang=settings.LANG):
    # news_list = get_news_list()

    return render_template( 'news.tpl', settings=settings, news_list=articles, lang=lang )

@app.route('/<lang>/news/article/<news_id>')
@app.route('/<lang>/news/article/<news_id>/')
def show_article(lang=settings.LANG):
    return render_template( 'article.tpl', settings=settings, lang=lang )

@app.route('/<lang>/products')
@app.route('/<lang>/products/')
@app.route('/<lang>/products/list')
@app.route('/<lang>/products/list/')
def show_products(lang=settings.LANG):
    from collections import Counter
    brand_count = dict(Counter(map(lambda x:x['brand'], products)))
    
    return render_template( 'products.tpl', settings=settings, product_list=products, brand_count=brand_count, lang=lang )


###############################################################
# should use Javascript instead to handle the brand filtering #
###############################################################
@app.route('/<lang>/products/brand/<brandname>')
@app.route('/<lang>/products/brand/<brandname>/')
def show_product_by_brand(brandname, lang=settings.LANG):
    from collections import Counter
    brand_count = dict(Counter(map(lambda x:x['brand'], products)))

    ## filter by selected product
    _products = filter(lambda x:x['brand'] == brandname.strip(), products)

    return render_template( 'products.tpl', settings=settings, product_list=_products, brand_count=brand_count )

@app.route('/<lang>/products/spec/<product_id>')
@app.route('/<lang>/products/spec/<product_id>/')
def show_spec(lang=settings.LANG):
    return render_template( 'product.tpl', settings=settings, lang=lang )

@app.route('/<lang>/about')
@app.route('/<lang>/about/')
def show_about(lang=settings.LANG):
    print '>>>>> render show_about in %s' % lang
    return render_template( 'about.tpl', settings=settings, lang=lang )

@app.route('/<lang>/download')
@app.route('/<lang>/download/')
def show_download(lang=settings.LANG):
    return render_template( 'download.tpl', settings=settings, lang=lang )

@app.route('/<lang>/contact')
@app.route('/<lang>/contact/')
def show_contact(lang=settings.LANG):
    return render_template( 'contact.tpl', settings=settings, lang=lang )

###############################
##           utils           ##
###############################




###############################
##         Databases         ##
###############################
def get_news_by_id(news_id):
    ## fetch db by news_id
    #...

    ## generate dict
    # ...

    return article
    
def get_news_list():

    ## generate list of dict
    # ...
    
    return articles



###############################
##         Databases         ##
###############################

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == "__main__":
    import getopt, sys

    port = 5000
    app.debug = False

    try:
        opts, args = getopt.getopt(sys.argv[1:],'p:d',['port=', 'debug'])
    except getopt.GetoptError:
        exit(2)

    for opt, arg in opts:
        if opt in ('-p', '--port'): port = int(arg.strip())
        elif opt in ('-d','--debug'): app.debug = True

    app.run(host='0.0.0.0', port=port)
