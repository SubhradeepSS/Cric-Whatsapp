import requests
from twilio.rest import Client
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


class get_Score:
    def __init__(self):
        self.url_get_all_matches = "https://cricapi.com/api/matches"
        self.get_score = "https://cricapi.com/api/cricketScore"
        self.apikey = ''
        self.unique_id_of_match = ''

    def get_unique_id(self):
        uri_params = {'apikey': self.apikey}
        response = requests.get(self.url_get_all_matches, uri_params)
        india_match_is_there = 0
        response_dict = response.json()

        for i in response_dict['matches']:
            if i['team-1'] == 'India' or i['team-2'] == 'India' and i['matchStarted']:
                today_date = datetime.today().strftime('%Y-%m-%d')
                if today_date == i['date'].split('T')[0]:
                    self.unique_id_of_match = i['unique_id']
                    india_match_is_there = 1
                    break
        if not india_match_is_there:
            self.unique_id_of_match = -1

        data_from_site = self.get_current_score()
        print(data_from_site)
        return data_from_site

    def get_current_score(self):
        data = ''
        if self.unique_id_of_match == -1:
            data = 'No India matches today'
        else:
            uri_params = {'apikey': self.apikey, 'unique_id': self.unique_id_of_match}
            response = requests.get(self.get_score, uri_params)
            response_dict = response.json()
            try:
                data = 'Score is :\n' + response_dict['stat'] + '\n' + response_dict['score']
            except KeyError as e:
                print(e)
        return data


def main():
    obj_score = get_Score()
    whatsapp_message = obj_score.get_unique_id()
    account_sid = ''
    account_auth_token = ''
    client = Client(account_sid, account_auth_token)
    client.messages.create(body=whatsapp_message, from_='whatsapp:+14155238886', to='whatsapp:+919436946555')


def regular_interval_scheduler():
    scheduler = BlockingScheduler()
    scheduler.add_job(main, 'interval', seconds=5)
    scheduler.start()

