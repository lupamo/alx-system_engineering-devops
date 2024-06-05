#!/usr/bin/python3
"""Using reddit API"""
import requests


def number_of_subscribers(subreddit):
    """
    A function that queries API data and returns the number of
    reddit subscribers
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    headers = {'User-Agent': 'VICTORY'}
    resp = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(str(subreddit)),
        headers=headers,
        allow_redirects=False
    )

    if resp.status_code != 200:
        return 0
    data = resp.json()
    return data.get('data').get('subscribers')
