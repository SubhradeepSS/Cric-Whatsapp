import requests
from datetime import datetime
import os

class get_Score:
    def __init__(self, country):
        self.url_get_all_matches = "https://cricapi.com/api/matches"
        self.get_score = "https://cricapi.com/api/cricketScore"
        self.apikey = ''
        self.unique_id_of_match = ''
        self.country = country

    def get_unique_id(self):
        uri_params = {'apikey': self.apikey}
        response = requests.get(self.url_get_all_matches, uri_params)
        match_is_there = 0
        response_dict = response.json()

        for i in response_dict['matches']:
            if i['team-1'] == self.country or i['team-2'] == self.country and i['matchStarted']:
                today_date = datetime.today().strftime('%Y-%m-%d')
                if today_date == i['date'].split('T')[0]:
                    self.unique_id_of_match = i['unique_id']
                    match_is_there = 1
                    break
        if not match_is_there:
            self.unique_id_of_match = -1

        data_from_site = self.get_current_score()
        print(data_from_site)
        return data_from_site

    def get_current_score(self):
        data = ''
        if self.unique_id_of_match == -1:
            data = f'No {self.country} matches today'
        else:
            uri_params = {'apikey': self.apikey, 'unique_id': self.unique_id_of_match}
            response = requests.get(self.get_score, uri_params)
            response_dict = response.json()
            try:
                data = 'Score is :\n' + response_dict['stat'] + '\n' + response_dict['score']
            except KeyError as e:
                print(e)
        return data
