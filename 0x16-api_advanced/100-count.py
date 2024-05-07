#!/usr/bin/python3
"""Reddit api module call to article"""
import requests


def count_words(subreddit, word_list, after=None, count=None):
    """
    queries the Reddit API, parses the title of all hot articles
    and prints a sorted count of given keywords (case-insensitive,
    delimited by spaces
    """

    if after is None:
        count = {word.lower(): 0 for word in word_list}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    resp = requests.get(url, params={'after': after},
                        headers={'user-agent': 'VICTORY'})
    if resp.status_code == 200:
        data = resp.json()

        for t in data['data']['children']:
            for word in t['data']['title'].split():
                for get_word in word_list:
                    if word.lower() == get_word.lower():
                        count[get_word.lower()] += 1

        after = data['data']['after']
        if after is None:
            sort = sorted(count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sort:
                if count > 0:
                    print("{}: {}".format(word, count))
        else:
            count_words(subreddit, word_list, after, count)
