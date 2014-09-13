# coding: utf-8

from cps import db

## create the tables and database
print 'create tables and database'
db.create_all()

from cps import User

## create some users
print 'create `admin` and `guest`'
admin = User('admin', 'admin@cps.com')
guest = User('guest', 'guest@cps.com')

## commit
db.session.add(admin)
db.session.add(guest)
db.session.commit()

print '-'*20,'commit','-'*20

## access the data in database
users = User.query.all()

print '''User.query.all() >''', users

admin = User.query.filter_by(username='admin').first()

print '''User.query.filter_by(username='admin').first() >''', admin
