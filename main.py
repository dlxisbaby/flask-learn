#coding:utf-8

from flask import Flask
from config import DevConfig,DEBUG
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)
#app.debug = DEBUG

class User(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    posts = db.relationship(
        'Post',
        backref = 'user',
        lazy = 'dynamic'
        )
    
    def __init__(self,username):
        self.username = username
    
    def __repr__(self):
        return "<User '{}'>".format(self.username)
    
class Post(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_data = db.Column(db.DateTime())
    user_id = db.Column(db.Integer(),db.ForeignKey('user.id'))
    comments = db.relationship(
        'Comment',
        backref = 'post',
        lazy = 'dynamic'
        )
    
    def __init__(self,title):
        self.title = title
        
    def __repr__(self):
        return "<Post '{}'>".format(self.title)
    
class Comment(db.model):
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.Integer(),ForeignKey='post.id')
    
    def __repr__(self):
        return "<Comment '{}'>".format(self.text[:15])
    
@app.route('/')
def home():
    return '<h1>Hello World</h1>'


if __name__ == "__main__":
    app.run()