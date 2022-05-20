#!/usr/bin/python3
"""Using a REST API returns information about employee ID TODO list progress"""


if __name__ == '__main__':
    import requests
    import sys
    import json

    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    all_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    all_todo = all_todo.json()
    json_file = {}
    list = []

    for user in users:
        for task in all_todo:
            if task.get('userId') == user.get('id'):
                dict = {"username": user.get('username'),
                        "task": task.get('title'),
                        "completed": task.get('completed')}
                list.append(dict)
        json_file[user.get('id')] = list

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(json_file, f)
