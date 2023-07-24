#!/usr/bin/python3
''' export data in the CSV format '''
from sys import argv
from requests import get
import csv


if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com'
    usr = get(api_url + '/users/' + argv[1]).json()['username']
    todos = get(api_url + '/todos?userId=' + argv[1]).json()
    with open('{}.csv'.format(argv[1]), mode='w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([argv[1], usr, todo['completed'], todo['title']])
