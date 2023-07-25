#!/usr/bin/python3
''' export data in json format '''
from sys import argv
from requests import get
import json


if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com'
    users = get(api_url + '/users/').json()
    todos = get(api_url + '/todos/').json()
    num, records = 0, list()
    id, user, all = users[num]['id'], users[num]['username'], dict()
    for todo in todos:
        if todo['userId'] != id:
            all[id] = records
            num += 1
            id, user = users[num]['id'], users[num]['username']
            records = list()
        records.append({'username': user, 'task': todo['title'],
                       'completed': todo['completed']})
    all[id] = records
    with open('todo_all_employees.json', mode='w') as fd:
        json.dump(all, fd)
