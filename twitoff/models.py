from twitoff import db 

class User(db.Model):
    """ Twitter Users Corresponding to Tweets """ 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "f' User {self.name}"
    

