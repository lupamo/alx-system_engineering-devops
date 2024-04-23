#!/usr/bin/python3
"""
a script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
and exports it to a csv
"""

import json
import requests
from sys import argv


def list_dic(url):
    """gets todo list of all users"""
    resp = requests.get(url + "/users")
    users = resp.json()

    data = {}
    for user in users:
        id = user["id"]
        resp = requests.get(url + f"/todos?userId={id}")
        todo = resp.json()

        user_t = []
        for t in todo:
            user_t.append({
                "task": t["title"],
                "completed": t["completed"],
                "username": user["username"]
            })
        data[id] = user_t
    return data


if __name__ == '__main__':
    users_url = "https://jsonplaceholder.typicode.com"
    data = list_dic(users_url)

    # writee the data to a json file
    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file, indent=4)
