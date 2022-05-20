#!/usr/bin/python3
"""Using REST API returns information about employee ID TODO list progress"""


if __name__ == '__main__':
    import requests
    import sys

    employee_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(employee_id)).json()
    all_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    all_todo = all_todo.json()
    user_name = user.get('name')
    user_id = user.get('id')
    tasks = []
    done_tasks = 0
    tasks_todo = 0

    for todo in all_todo:
        if todo.get('userId') == int(employee_id):
            tasks_todo += 1
            if todo.get('completed') is True:
                done_tasks += 1
                tasks.append(todo.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(
        user_name,
        done_tasks,
        tasks_todo))
    for task in tasks:
        print('\t', task)
