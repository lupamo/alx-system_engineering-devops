#!/usr/bin/python3
"""Reddit api module call recursively"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    function that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"count": count, "after": after}
    headers = {"User-Agent": "My-User-Agent"}
    subs = requests.get(url, params, headers=headers, allow_redirects=False)

    if subs.status_code >= 400:
        return None
    lst = hot_list + [child.get("data").get("title")
                      for child in subs.json()
                      .get("data")
                      .get("children")]
    get_info = subs.json()
    if not get_info.get("data").get("after"):
        return lst

    return recurse(subreddit, lst, get_info.get("data").get("count"),
                   get_info.get("data").get("after"))
