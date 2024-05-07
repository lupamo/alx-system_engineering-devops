#!/usr/bin/python3
"""Reddit api module call"""
import requests


def top_ten(subreddit):
    """
    A reddit function that ptints tittle
    of the first ten host for a given subreddit
    """
    headers = {'User-Agent': 'VICTORY'}
    url =f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print("None")


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
