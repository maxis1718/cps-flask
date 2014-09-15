# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, make_response, Response, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy_i18n import make_translatable, translation_base





###############################
##          Model            ##
###############################

db = SQLAlchemy(app)
make_translatable(SQLAlchemy.orm.mapper)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class News(object):

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(256), unique=False)
    publish_time = db.Column(db.DateTime, unique=False)

    def __init__(self, image_url, publish_time):
        self.image_url = image_url
        self.publish_time = publish_time
        
        
    def __repr__(self):
        return '<News %r>' % self.id



