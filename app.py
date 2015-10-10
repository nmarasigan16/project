import tweepy
import json
import os
from flask import Flask
from flask import render_template
from flask import request
from flask import abort
app = Flask(__name__)
app.debug = True

with open('secrets/oauth.json', 'r') as secrets:
    secrets = json.load(secrets)
    SECRET_KEY = secrets['SECRET_KEY']
    consumer_token = secrets['CONSUMER_KEY']
    consumer_secret = secrets['CONSUMER_SECRET']

callback_url = "http://localhost:5000/oauth"

auth = tweepy.OAuthHandler(consumer_token, consumer_secret, callback_url)
redirect_url = auth.get_authorization_url()
print(redirect_url)
auth.secure = True

if(not os.path.isfile('secrets/tokens.json')):
    with open('secrets/tokens.json', 'w') as secrets:
        json.dump([], secrets)

@app.route('/', methods=["GET"])
def main():
    return render_template('index.html', redirect_url=redirect_url)

@app.route('/oauth', methods=["GET"])
def oauth():
    with open('secrets/tokens.json', 'r') as secrets_file:
        secrets = json.load(secrets_file)
    data = {
            "oauth_token": request.args.get('oauth_token'),
            "oauth_verifier": request.args.get('oauth_verifier')
            }
    secrets.append(data)
    with open('secrets/tokens.json', 'w') as secrets_file:
        json.dump(secrets, secrets_file)
    return render_template('oauth.html')
     
@app.route('/get_keys', methods=["GET"])
def get_keys():
    if(requests.args.get('key') == SECRET_KEy):
        with open('secrets/tokens.json', 'r') as secrets:
            return secrets.read()
    abort(403)

if __name__ == "__main__":
    app.run()
