import requests, datetime, pprint
from datetime import datetime, timedelta
from pprint import pprint


def get_question(days, tag):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    # print(end_date)
    # print(start_date)
    PARAMS = {'started': start_date, 'ended': end_date, 'tagged': tag, 'site': 'stackoverflow'}
    resp = requests.get('https://api.stackexchange.com/2.3/questions', params=PARAMS)
    # print(resp)
    for question in resp.json().get('items'):
        pprint(('Question: ' + question['title']))
        pprint('Tags: ' + str(question['tags']))
        print('-------------------------')


get_question(2, 'python')
