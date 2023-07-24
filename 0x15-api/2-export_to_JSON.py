#!/usr/bin/python3
''' export data in the CSV format '''
from sys import argv
from requests import get
import json


if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com'
    usr = get(api_url + '/users/' + argv[1]).json()['username']
    todos = get(endpoint + '/todos?userId=' + argv[1]).json()
    record, user_data, group = {}, {}, list()
    for todo in todos:
        record['task'] = todo['title']
        record['completed'] = todo['completed']
        record['username'] = usr
        group.append(record)
        record = dict()
    user_data[argv[1]] = group
    with open('{}.json'.format(argv[1]), mode='w') as fd:
        json.dump(user_data, fd)
