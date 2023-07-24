#!/usr/bin/python3
"""Gather data from an API"""


if __name__ == '__main__':
    from requests import get
    from sys import argv, exit
    try:
        id_val = argv[1]
        emp_id = int(id_val)
    except ValueError:
        exit()

api_url = 'https://jsonplaceholder.typicode.com'
user_url = '{api}/users/{id}'.format(api=api_url, id=emp_id)
todo_url = '{userUrl}/todos'.format(userUrl=user_url)

try:
    user_js = get(user_url).json()
    todo_js = get(todo_url).json()
except ValueError:
    print('Not a valid JSON')

if user_js and todo_js:
    EMPLOYEE_NAME = user_js[0].get('name')
    TOTAL_NUMBER_OF_TASKS = len(todo_js)
    NUMBER_OF_DONE_TASKS = sum(item.get("completed")
                               for item in todo_js if item)
    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME,
                  NUMBER_OF_DONE_TASKS,
                  TOTAL_NUMBER_OF_TASKS))
    for todo in todo_js:
        TASK_TITLE = todo.get('title')
        if todo.get("completed"):
            print("\t {}".format(TASK_TITLE))
