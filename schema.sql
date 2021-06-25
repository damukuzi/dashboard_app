DROP TABLE IF EXISTS extracted_data;

CREATE TABLE IF NOT EXISTS extracted_data (
    tweet_id INT AUTO_INCREMENT PRIMARY KEY,
    inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    source VARCHAR(255) NOT NULL,
    original_text VARCHAR(255) NOT NULL,
    polarity INT NOT NULL,
    subjectivity INT NOT NULL,
    lang VARCHAR(255) NOT NULL,
    favorite_count INT,
    retweet_count INT ,
    original_author VARCHAR(255),
    followers_count INT,
    friends_count INT,
    hashtags VARCHAR(255),
    user_mentions VARCHAR(255),
    place VARCHAR(255)
)  ENGINE=INNODB;

