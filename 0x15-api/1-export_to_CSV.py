#!/usr/bin/python3
"""
Using task 0 extend script to xport data in the CSV format
"""

import requests
    import sys
    import csv
    
if __name__ == '__main__':
    """"""
    employee_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(employee_id)).json()
    all_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    .json()
    user_name = user.get('username')
    file = employee_id + '.csv'

    with open(file, mode='w') as f:
        write = csv.writer(f, delimiter=',', quotechar='"',
                           quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in all_todo:
            if task.get('userId') == int(employee_id):
                write.writerow([employee_id, user_name,
                                str(task.get('completed')), task.get('title')])
