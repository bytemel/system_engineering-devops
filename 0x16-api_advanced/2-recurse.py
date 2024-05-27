#!/usr/bin/python3
"""
Recurse function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=''):
    """Returns a list containing the titles of
    all hot articles for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Google Chrome Version 120.0.6099.217'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        if data['data']['after'] is not None:
            return recurse(subreddit, hot_list, data['data']['after'])
        return hot_list
    else:
        return None
