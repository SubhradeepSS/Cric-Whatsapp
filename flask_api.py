from flask import Flask, request
from matchStats import fetch_stats

app = Flask(__name__)

@app.route('/<team_name>', methods = ['GET'])
def view(team_name):
    return fetch_stats(team_name)[1]

app.run(debug=True)