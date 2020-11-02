from twilio.rest import Client
import requests
from tokens import *

def fetch_stats(team_name):
    MATCH_URL = CRIC_API['matches_url']
    CRIC_API_KEY = CRIC_API['key']
    SCORE_URL = CRIC_API['score_url']
    
    def getScore(match_id):
        try:
            score_request = requests.get(SCORE_URL, params={ 'unique_id': match_id, 'apikey': CRIC_API_KEY })
            return score_request.text
        except Exception as e:
            return e

    try:
        match_request = requests.get(MATCH_URL, params={ 'apikey': CRIC_API_KEY })
        matches = match_request.json()['matches']

        for match in matches:
            if match['team-1'] == team_name or match['team-2'] == team_name:
                return getScore(match['unique_id'])
    
    except Exception as e:
        return e


def sendWPMsg(team_name):
    whatsapp_message = fetch_stats(team_name)
    account_sid = TWILIO['account_sid']
    account_auth_token = TWILIO['account_auth_token']

    try:
        client = Client(account_sid, account_auth_token)
        client.messages.create(body=whatsapp_message, from_=f'whatsapp:{TWILIO["bot_no"]}', to=f'whatsapp:{WHATSAPP_NO}')
    
    except Exception as e:
        print(e)


team = input('Enter the name of the team you want to know stats about: ')
sendWPMsg(team)