from twitoff import db 

class User(db.Model):
    """ Twitter Users Corresponding to Tweets """ 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    tweets = db.relationship('Tweet', backref='user', lazy='dynamic')

    def __repr__(self):
        return f" User {self.name}"
    

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Tweet {self.text}"


