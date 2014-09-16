# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, make_response, Response, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
# from flask.ext.admin import Admin
# from flask.ext.admin.contrib.sqla import ModelView
from sqlalchemy_i18n import make_translatable, translation_base, Translatable
from datetime import datetime
import settings

app = Flask(__name__)

## Setup SQLAlchemy
## For a relative file path: 3 slashes,  e.g., sqlite:///test.db
## For an absolute file path: 4 slashes, e.g., sqlite:////tmp/test.db
## ref. http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html#sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % 'test.db'


###############################
##          Model            ##
###############################

db = SQLAlchemy(app)
make_translatable()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


# ========= News ==========

class News(db.Model, Translatable):
    __tablename__ = 'news'

    __translatable__ = {
        'locales': ['en', 'zh']
    }

    locale = 'zh'  # this defines the default locale

    id = db.Column(db.Integer, autoincrement = True , primary_key=True)
    image_url = db.Column(db.String(256))
    publish_time = db.Column(db.DateTime)

    def __init__(self, image_url="", publish_time=datetime.now()):
        self.image_url = image_url
        self.publish_time = publish_time

    def __repr__(self):
        return '<News %r>' % self.id

class NewsTranslation(translation_base(News)):
    
    __tablename__ = 'news_translation'
    
    description = db.Column(db.String(255))
    content = db.Column( db.Text)
    title = db.Column( db.Text)

# admin = Admin(app)
# admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(News, db.session))
# admin.add_view(ModelView(NewsTranslation, db.session))

# ========= Product Type ==========

class ProductType(db.Model, Translatable):
    __tablename__ = 'product_type'

    __translatable__ = {
        'locales': ['en', 'zh']
    }

    locale = 'zh'  # this defines the default locale

    id = db.Column(db.Integer, autoincrement = True , primary_key=True)
    product =  db.relationship('Product', backref='productType',
                                lazy='joined')

    def __init__(self):
        pass

    def __repr__(self):
        return '<ProductType %r>' % self.id

class ProductTypeTranslation(translation_base(ProductType)):
    
    __tablename__ = 'product_type_translation'
    
    name = db.Column( db.String(80) ) 

# ========= Brand ==========

class Brand(db.Model, Translatable):
    __tablename__ = 'brand'

    __translatable__ = {
        'locales': ['en', 'zh']
    }

    locale = 'zh'  # this defines the default locale

    id = db.Column(db.Integer, autoincrement = True , primary_key=True)
    product =  db.relationship('Product', backref='brand',
                                lazy='joined')

    def __init__(self):
        pass

    def __repr__(self):
        return '<Brand %r>' % self.id

class BrandTranslation(translation_base(Brand)):
    
    __tablename__ = 'brand_translation'
    
    name = db.Column( db.String(80) ) 

# ========= Product ==========

class Product(db.Model, Translatable):
    __tablename__ = 'product'

    __translatable__ = {
        'locales': ['en', 'zh']
    }

    locale = 'zh'  # this defines the default locale

    id = db.Column(db.Integer, autoincrement = True , primary_key=True)
    image_url = db.Column(db.String(256))
    publish_time = db.Column(db.DateTime)
    product_type_id = db.Column(db.Integer, db.ForeignKey('product_type.id'))
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))

    def __init__(self, image_url="", publish_time=datetime.now(), product_type_id=0 , brand_id=0):
        self.image_url = image_url
        self.publish_time = publish_time
        self.product_type_id = product_type_id
        self.brand_id = brand_id

    def __repr__(self):
        return '<Product %r>' % self.id

class ProductTranslation(translation_base(Product)):
    
    __tablename__ = 'product_translation'
    
    description = db.Column(db.String(255))
    content = db.Column( db.Text)
    title = db.Column( db.Text)





###############################
##         Locations         ##
###############################

@app.route('/')
@app.route('/<lang>')
@app.route('/<lang>/')
def index(lang=settings.LANG):
    return render_template( 'index.tpl', settings=settings, lang=lang, is_index=True )

@app.route('/<lang>/news')
@app.route('/<lang>/news/')
@app.route('/<lang>/news/list')
@app.route('/<lang>/news/list/')
def show_news(lang=settings.LANG):
    # news_list = get_news_list()
    news_arr = News.query.all()

    
    return_arr = []
    for item in news_arr:
        dic = {}
        dic['title'] = item.translations[lang].title
        dic['content'] = item.translations[ lang ].content
        dic['description'] = item.translations[lang].description
        dic['id'] = item.id
        dic['image_url'] = item.image_url
        return_arr.append( dic )


    return render_template( 'news.tpl', settings=settings, news_list=return_arr, lang=lang )

@app.route('/<lang>/news/article/<news_id>')
@app.route('/<lang>/news/article/<news_id>/')
def show_article(lang=settings.LANG):
    return render_template( 'article.tpl', settings=settings, lang=lang )

@app.route('/<lang>/products')
@app.route('/<lang>/products/')
@app.route('/<lang>/products/list')
@app.route('/<lang>/products/list/')
@app.route('/<lang>/products/list/brand/')
@app.route('/<lang>/products/list/brand/')
def show_products(lang=settings.LANG):

    product_arr = Product.query.all()

    brand_arr = Brand.query.all()

    return render_template( 'products.tpl', settings=settings,brand_count=brand_arr, product_list=product_arr, lang=lang )

@app.route('/<lang>/products/list/brand/<brandname>')
@app.route('/<lang>/products/list/brand/<brandname>/')
def show_product_by_brand(brandname, lang=settings.LANG):
    from collections import Counter
    brand_count = dict(Counter(map(lambda x:x['brand'], products)))

    ## filter by selected product
    _products = filter(lambda x:x['brand'] == brandname.strip(), products)

    return render_template( 'products.tpl', settings=settings, product_list=_products, brand_count=brand_count )

@app.route('/<lang>/products/<product_id>')
def show_spec(lang=settings.LANG, product_id=1):
    product = Product.query.filter_by(id=product_id).first()

    return render_template( 'product.tpl', settings=settings, lang=lang, product=product )

@app.route('/<lang>/about')
@app.route('/<lang>/about/')
def show_about(lang=settings.LANG):
    print '>>>>> render show_about in %s' % lang
    return render_template( 'about.tpl', settings=settings, lang=lang )

@app.route('/<lang>/download')
@app.route('/<lang>/download/')
def show_download(lang=settings.LANG):
    softwares = [{
        "title_zh":"Android 版驅動程式",
        "title_en":"Driver for Android",
        "filename":"driver-3.0.3-for-android.zip",
    },{
        "title_zh":"iPhone 版驅動程式",
        "title_en":"Driver for iPhone",
        "filename":"driver-2.0.1-for-iphone.zip",
    }]
    return render_template( 'download.tpl', settings=settings, lang=lang, softwares=softwares )

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






