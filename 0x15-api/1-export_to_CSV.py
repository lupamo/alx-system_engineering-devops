#!/usr/bin/python3
"""
a script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
and exports it to a csv
"""

import csv
import requests
from sys import argv


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
    # Open the CSV file in write mode
    with open("{}.csv".format(user_id), 'w') as file:
        # Write each task to the CSV file
        for t in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(user_id, user_name, t.get('completed'),
                               t.get('title')))
