import requests
from datetime import datetime
class Score:
    def __init__(self):
        self.url_all_matches="http://cricapi.com/api/matches"
        self.url_score="http://cricapi.com/api/cricketScore"
        self.api_key="your cric api key" #your cric api key is the key that you will get after signing up an account in cricapi
        self.id=""
    
    def get_id(self):
        uri_params={"apikey":self.api_key}
        response=requests.get(self.url_all_matches,params=uri_params)
        response_dict=response.json()
        id_found=0
        for i in response_dict['matches']:
            if(i['team-1']=='India' or i['team-2']=='India' and i['matchStarted']):
                today_date=datetime.today().strftime('%Y-%m-%d')
                if today_date==i['date'].split('T')[0]:
                    id_found=1
                    self.id=i['unique_id']
                    break
        if not id_found:
            self.id=-1
        data=self.get_score(self.id)
        return data

    def get_score(self,id):
        data=''
        if id==-1:
            data='No live India matches'
        else:
            uri_params={"apikey":self.api_key,"unique-id":id}
            response=requests.get(self.get_score,params=uri_params)
            data_json=response.json()
            try:
                data="Score :"+"\n"+data_json['stat']+"\n"+data_json['score']
            except KeyError as e:
                data="Something went wrong!!"+"\n"+"Please try again"
        return data

if __name__ == "__main__":
    match=Score()
    send=match.get_id()
    print(send)
    from twilio.rest import Client
    account_sid='your twilio account sid'  #Sid for your Twilio account
    auth_token='your twilio account authorisation token' #The token for your Twilio account
    client=Client(account_sid,auth_token)
    message=client.messages.create(body=send,from_='whatsapp:+14155238886',to='whatsapp:+919436946555')