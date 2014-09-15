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
# db.session.add(admin)
# db.session.add(guest)
# db.session.commit()


print "creat news"
news1 = News("http://xxx.yyy.zzz/i.jpg", datetime.now() )
news1.translations['zh'].title = "中文"


db.session.add(news1)
db.session.commit()


print '-'*20,'commit','-'*20

## access the data in database
users = User.query.all()

print '''User.query.all() >''', users

admin = User.query.filter_by(username='admin').first()

print '''User.query.filter_by(username='admin').first() >''', admin
