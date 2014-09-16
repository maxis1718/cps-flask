# coding: utf-8
from datetime import datetime
from cps import db

## create the tables and database
print 'create tables and database'
db.create_all()

from cps import User
from cps import News

## create some users
print 'create `admin` and `guest`'
admin = User('admin', 'admin@cps.com')
guest = User('guest', 'guest@cps.com')

## commit
db.session.add(admin)
db.session.add(guest)
db.session.commit()


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


print '-'*20,'commit','-'*20

## access the data in database
news_arr = News.query.all()

print '''User.query.all() >''', [ x.translations['en'].title for x in news_arr ]




