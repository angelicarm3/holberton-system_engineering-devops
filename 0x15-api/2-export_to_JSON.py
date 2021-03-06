#!/usr/bin/python3
"""Using a REST API returns information about employee ID TODO list progress"""


if __name__ == '__main__':
    import requests
    import sys
    import json

    employee_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(employee_id)).json()
    all_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    all_todo = all_todo.json()
    user_name = user.get('username')
    json_file = {}
    list = []

    for task in all_todo:
        if task.get('userId') == int(employee_id):
            dict = {"task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": user.get('username')}
            list.append(dict)
    json_file[employee_id] = list

    filename = employee_id + '.json'
    with open(filename, mode='w') as f:
        json.dump(json_file, f)
