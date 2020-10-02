from twilio.rest import Client
from tokens import TWILIO, WHATSAPP_NO
from matchStats import fetch_stats

def sendWPMsg(team_name):
    whatsapp_message, _ = fetch_stats(team_name)
    account_sid = TWILIO['account_sid']
    account_auth_token = TWILIO['account_auth_token']

    try:
        client = Client(account_sid, account_auth_token)
        client.messages.create(body=whatsapp_message, from_=f'whatsapp:{TWILIO["bot_no"]}', to=f'whatsapp:{WHATSAPP_NO}')
    
    except Exception:
        print("Error in sendWPMsg function!!!")

sendWPMsg('Chennai Super Kings')