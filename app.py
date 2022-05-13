import os

from flask import Flask, request, jsonify, render_template
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant

app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/token')
def generate_token():
    # get credentials from environment variables
    TWILIO_ACCOUNT_SID = 'AC404f7bbb2a8b4f40f282c957c5f8c477'
    TWILIO_SYNC_SERVICE_SID = 'IS3c04777aafcbc96ab285ed09e6d608fd'
    TWILIO_API_KEY = 'SKd132e020fbda4257b06f91f1a6abd9d6'
    TWILIO_API_SECRET = 'nhid4oItz2C1KeiubAJ5Dj9dRjIEL1FN'
    account_sid = TWILIO_ACCOUNT_SID
    api_key = TWILIO_API_KEY
    api_secret = TWILIO_API_SECRET
    sync_service_sid = TWILIO_SYNC_SERVICE_SID
    username = request.args.get('username', fake.user_name())

    # create access token with credentials
    token = AccessToken(account_sid, api_key, api_secret, identity=username)
    # create a Sync grant and add to token
    sync_grant = SyncGrant(sync_service_sid)
    token.add_grant(sync_grant)
    return jsonify(identity=username, token=token.to_jwt())

if __name__ == "__main__":
    app.run(host='localhost', port='5001', debug=True)