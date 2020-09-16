from twitoff import db 

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    screen_name = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String)
    followers_count = db.Column(db.Integer, nullable=False)
    tweets = db.relationship('Tweet', backref='user', lazy=True)

class Tweet(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey("user.id"))
    full_text = db.Column(db.String(500))
    embedding = db.Column(db.PickleType)
    


