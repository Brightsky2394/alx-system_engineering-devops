#!/usr/bin/python3
"""Queries the Reddit API and
returns a list containing the
titles of all hot articles for
a given subreddit.
"""
from requests import get


def recurse(subreddit, hot_list=[], after=''):
    """Returns a list containing the titles of all
    hot articles for a given subreddit.
    """
    base_url = 'https://www.reddit.com'
    api_url = '{base}/r/{sub}/hot.json'.format(base=base_url, sub=subreddit)

    user_agent = {'user-agent': 'my user agent 1.2'}

    payload = {'after': after, 'limit': '100'}

    response = requests.get(api_uri, headers=user_agent,
                            params=payload, allow_redirects=False)
    if res.status_code == 200:
        results = response.json()
        hot_posts = results.get('data').get('children')
        after = results.get('data').get('after')

        for post in hot_posts:
            hot_list.append(post.get('data').get('title'))

        if after is not None:
            recurse(subreddit, hot_list, after)

        return hot_list

    return None
