from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd

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
    csv_data=pd.read_csv('processed_tweet_data.csv')
    csv_data=csv_data.values.tolist()
    for row in csv_data:
        data=extracted_data(source=row[0],original_text=row[1],polarity=row[2],subjectivity=row[3],lang=row[4],
        favorite_count=row[5],retweet_count=row[6],original_author=row[7],followers_count=row[8],friends_count=row[9],
        hashtags=row[10],user_mentions=row[11],place=row[12])
        db.session.add(data)
        db.session.commit()

@app.route("/")  # this sets the route to this page
def home():
	return "Hello! this is the main page <h1>HELLO</h1>"  # some basic inline html

@app.route("/twitterdata")  # this sets the route to this page
def twitterdata():
	return "Hello! this is a placeholder for twitter data page <h1>HELLO</h1>"  # some basic inline html

if __name__ == "__main__":
    app.run()