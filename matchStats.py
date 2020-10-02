import requests
from tokens import CRIC_API

MATCH_URL = CRIC_API['matches_url']
CRIC_API_KEY = CRIC_API['key']
SCORE_URL = CRIC_API['score_url']


def fetch_stats(team_name):

    def getScore(match_id):
        try:
            score_request = requests.get(SCORE_URL, params={ 'unique_id': match_id, 'apikey': CRIC_API_KEY })
            return score_request.text, score_request.json()
        except:
            return "Error or api(score fetch) problem!!!"

    try:
        match_request = requests.get(MATCH_URL, params={ 'apikey': CRIC_API_KEY })
        matches = match_request.json()['matches']

        for match in matches:
            if match['team-1'] == team_name or match['team-2'] == team_name:
                return getScore(match['unique_id'])
    
    except:
        return "Error from API fetching!!!"
