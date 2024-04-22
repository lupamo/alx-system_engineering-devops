#!/usr/bin/python3
"""
a script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from sys import argv
import requests

if __name__ == '__main__':
    user_id = argv[1]  # argv so that we enter users id as argument
    users_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{users_url}/{user_id}"

    with requests.get(url) as response:
        user_name = response.json().get('name')
        # extracting employee name using json

    todos = f"{url}/todos"  # getting todos url

    with requests.get(todos) as response:
        tasks = response.json()

    completed_task = [task for task in tasks if task.get('completed')]
    complete = len(completed_task)

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, complete, len(tasks)))
    for t in completed_task:
        print("\t " + t.get("title"))
