from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///twitter_data.sqlite3'

db = SQLAlchemy(app)
class extracted_data(db.Model):
    tweet_id = db.Column(db.Integer, primary_key=True)
    inserted_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    source = db.Column(db.String(100), nullable=False)
    original_text = db.Column(db.String(100), nullable=False)
    polarity = db.Column(db.Integer, nullable=False)
    subjectivity = db.Column(db.Integer, nullable=False)
    lang = db.Column(db.String(100), nullable=False)
    favorite_count = db.Column(db.Integer, nullable=True)
    retweet_count = db.Column(db.Integer, nullable=True)
    original_author = db.Column(db.String(100), nullable=True)
    followers_count = db.Column(db.Integer, nullable=True)
    friends_count = db.Column(db.Integer, nullable=True)
    hashtags = db.Column(db.String(100), nullable=True)
    user_mentions = db.Column(db.String(100), nullable=True)
    place = db.Column(db.String(100), nullable=True)

#run below only once to create the db initially
#db.create_all()

def insert_data():
    pass

@app.route("/")  # this sets the route to this page
def home():
	return "Hello! this is the main page <h1>HELLO</h1>"  # some basic inline html

@app.route("/twitterdata")  # this sets the route to this page
def twitterdata():
	return "Hello! this is a placeholder for twitter data page <h1>HELLO</h1>"  # some basic inline html

if __name__ == "__main__":
    app.run()