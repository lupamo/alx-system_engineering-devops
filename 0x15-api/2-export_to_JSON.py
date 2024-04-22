#!/usr/bin/python3
"""
a script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
and exports it to a csv
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]  # argv so that we enter users id as argument
    users_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{users_url}/{user_id}"

    with requests.get(url) as response:
        # extracting employee name using json
        user_name = response.json().get('username')

        todos = f"{url}/todos"  # getting todos url
        
    with requests.get(todos) as response:
        tasks = response.json()

    dic  = {user_id: []}
    for t in tasks:
        dic[user_id].append({
            "task": t.get('title'),
            "completed": t.get('completed'),
            "username": user_name
		})
    with open('{}.json'.format(user_id), 'w') as file:
        json.dump(dic, file, indent=4)
