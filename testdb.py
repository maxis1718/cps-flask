# coding: utf-8
from datetime import datetime
from cps import db

## create the tables and database
print 'create tables and database'
db.create_all()

from cps import User
from cps import News
from cps import ProductType
from cps import Brand
from cps import Product

## create some users
print 'create `admin` and `guest`'
admin = User('admin', 'admin@cps.com')
guest = User('guest', 'guest@cps.com')

## commit
# db.session.add(admin)
# db.session.add(guest)
# db.session.commit()


print "creat news"
news1 = News("images/iPhone6.png", datetime.now() )
news1.translations['zh'].title = u"iPhone 6: 豈止於大"
news1.translations['en'].title = u"iPhone 6: Not only big"
news1.translations['zh'].description = u'<div>新手機上市</div>'
news1.translations['en'].description = u'<div>New iPhone</div>'
news1.translations['en'].content = u'<div>Latest iphone</div>'
news1.translations['zh'].content = u'<div>不只外型變大，更在各方面都顯著提升</div>'

news2 = News("images/samsung_note4.png", datetime.now() )
news2.translations['zh'].title = u"Galaxy Note 5: 豈止於大"
news2.translations['en'].title = u"iPhone 6: Not only big"
news2.translations['zh'].description = u'<div>新手機上市</div>'
news2.translations['en'].description = u'<div>New iPhone</div>'
news2.translations['en'].content = u'<div>Latest iphone</div>'
news2.translations['zh'].content = u'<div>不只外型變大，更在各方面都顯著提升</div>'


db.session.add(news1)
db.session.add(news2)
db.session.commit()

brand1 = Brand()
brand1.translations['zh'].name = u"蘋果"
brand1.translations['en'].name = u"Apple"
brand2 = Brand()
brand2.translations['zh'].name = u"索泥"
brand2.translations['en'].name = u"Sony"
db.session.add( brand1 )
db.session.add( brand2 )
db.session.commit()

product_type1 = ProductType()
product_type1.translations['zh'].name = u"一般手機"
product_type1.translations['en'].name = u"Phone"
product_type2 = ProductType()
product_type2.translations['zh'].name = u"配件"
product_type2.translations['en'].name = u"Accesory"
db.session.add( product_type1 )
db.session.add( product_type2 )
db.session.commit()

product1 = Product( image_url="images/iPhone6.png", publish_time=datetime.now(), product_type_id=1 , brand_id=1 , related_product_id=0)
product1.translations['zh'].title = u"iPhone 6"
product1.translations['en'].title = u"iPhone 6"
product1.translations['zh'].description = u'<div>新手機上市</div>'
product1.translations['en'].description = u'<div>New iPhone</div>'
product1.translations['en'].content = u'<div>Latest iphone</div>'
product1.translations['zh'].content = u'<div>不只外型變大，更在各方面都顯著提升</div>'

product2 = Product( image_url="images/iPhone6.png", publish_time=datetime.now(), product_type_id=1 , brand_id=1, related_product_id=0 )
product2.translations['zh'].title = u"iPhone 7"
product2.translations['en'].title = u"iPhone 7"
product2.translations['zh'].description = u'<div>新手機上市</div>'
product2.translations['en'].description = u'<div>New iPhone</div>'
product2.translations['en'].content = u'<div>Latest iphone</div>'
product2.translations['zh'].content = u'<div>不只外型變大，更在各方面都顯著提升</div>'


product3 = Product( image_url="images/iPhone6.png", publish_time=datetime.now(), product_type_id=2 , brand_id=2, related_product_id=2 )
product3.translations['zh'].title = u"iPhone 7: 耳機"
product3.translations['en'].title = u"iPhone 7 earphone"
product3.translations['zh'].description = u'<div>新耳機上市</div>'
product3.translations['en'].description = u'<div>New iPhone Earphone</div>'
product3.translations['en'].content = u'<div>Latest iphone</div>'
product3.translations['zh'].content = u'<div>不只外型變大，更在各方面都顯著提升</div>'


db.session.add( product1 )
db.session.add( product2 )
db.session.add( product3 )
db.session.commit()
print '-'*20,'Done','-'*20


pp = Product.query.filter_by(id=2).first()
print pp.translations['zh'].title
print pp.brand.translations['zh'].name
print pp.productType.translations['zh'].name






