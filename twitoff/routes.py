from flask import render_template, jsonify, request
from twitoff.models import User, Tweet
from twitoff import db, app
from twitoff.services.twitter_service import api as twitter_api_client
from twitoff.services.basilica_service import connection as basilica_api_client


@app.route("/")
def index():
    return render_template("prediction.html")


@app.route("/predict", methods=["POST"])
def predict():
    print("PREDICT ROUTE...")
    print("FORM DATA:", dict(request.form))
    #> {'screen_name_a': 'elonmusk', 'screen_name_b': 's2t2', 'tweet_text': 'Example tweet text here'}
    screen_name_a = request.form["screen_name_a"]
    screen_name_b = request.form["screen_name_b"]
    tweet_text = request.form["tweet_text"]

    print("-----------------")
    print("FETCHING TWEETS FROM THE DATABASE...")
   
    #TODO

    print("-----------------")
    print("TRAINING THE MODEL...")
    
    # classifier = LogisticRegression()
    # TODO: classifier.fit(___________, ___________)

    print("-----------------")
    print("MAKING A PREDICTION...")

    # TODO
    
    return render_template("results.html",
        screen_name_a=screen_name_a,
        screen_name_b=screen_name_b,
        tweet_text=tweet_text,
        screen_name_most_likely="TODO" 
    )


@app.route("/users/<screen_name>/fetch")
def fetch_user(screen_name=None):
    print(screen_name)

    twitter_user = twitter_api_client.get_user(screen_name)
    
    # get existing user from the db or initialize a new one:
    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)

    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    db_user.location = twitter_user.location
    db_user.followers_count = twitter_user.followers_count
    
    db.session.add(db_user)
    db.session.commit()
    #breakpoint()
    # return "OK"
    #return render_template("user.html", user=db_user, tweets=statuses) # tweets=db_tweets
    tweets = twitter_api_client.user_timeline(screen_name, tweet_mode="extended", count=300)
    print("TWEETS COUNT:", len(tweets))
    
    # basilica_api = basilica_api_client()

    all_tweet_texts = [tweet.full_text for tweet in tweets]
    embeddings = list(basilica_api_client.embed_sentences(all_tweet_texts, model="twitter"))
    print("NUMBER OF EMBEDDINGS", len(embeddings))

    for index, tweet in enumerate(tweets):
        print(index)
        print(tweet.full_text)
        print("----")
        
        embedding = embeddings[index]
        
        # get existing tweet from the db or initialize a new one:
        db_tweet = Tweet.query.get(tweet.id) or Tweet(id=tweet.id)

        db_tweet.user_id = tweet.author.id # or db_user.id
        db_tweet.full_text = tweet.full_text
        db_tweet.embedding = embedding
        db.session.add(db_tweet)
        
    db.session.commit()
    # #breakpoint()
    return "OK"
    # #return render_template("user.html", user=db_user, tweets=statuses) # tweets=db_tweets