#Handle spotify imports
import spotipy
from spotipy import oauth2

#Handle flask imports
from flask import Flask, request
from flask_restful import Resource, Api
import json
from flask_jsonpify import jsonify
from requests import get, put

cid = ''
secret = ''
uri = 'https://example.com/callback/'
scope = 'user-library-read user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming'

app = Flask(__name__)
api = Api(app)

@app.route('/ping')
def ping():
    return 'Done'

@app.route('/play', methods=['GET'])
def play_music():
    token_info = spotipy.util.prompt_for_user_token(username='main', scope=scope, client_id=cid, client_secret=secret, redirect_uri=uri)
    sp = spotipy.Spotify(token_info)

    deviceId = request.args.get('deviceId')
    uriToPlay = request.args.get('uriToPlay')
    volume = int(request.args.get('volume'))

    sp.volume(volume, deviceId)
    sp.start_playback(deviceId, uriToPlay)
    sp.shuffle(True, deviceId)
    
    return ('', 200)

@app.route('/pause', methods=['GET'])
def pause_music():
    token_info = spotipy.util.prompt_for_user_token(username='main', scope=scope, client_id=cid, client_secret=secret, redirect_uri=uri)
    sp = spotipy.Spotify(token_info)

    deviceId = request.args.get('deviceId')

    sp.pause_playback(deviceId)
    
    return ('', 200)

if __name__ == '__main__':
     app.run(port='8001', host='0.0.0.0')