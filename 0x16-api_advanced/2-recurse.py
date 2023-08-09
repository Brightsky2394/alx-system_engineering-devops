#!/usr/bin/python3
"""Queries the Reddit API """
from requests import get


def recurse(subreddit, hot_list=[], after=''):
    """Returns a list containing the titles of all
    hot articles for a given subreddit.
    """
    # Set the Default URL strings
    base_url = 'https://www.reddit.com'
    api_url = '{base}/r/{sub}/hot.json'.format(base=base_url, sub=subreddit)

    # Set an User-Agent
    user_agent = {'user-agent': 'my user agent 1.2'}

    # Set the Query Strings to Request
    payload = {'after': after, 'limit': '100'}

    # Get the Response of the Reddit API
    res = get(api_url, headers=user_agent,
              params=payload, allow_redirects=False)

    # Checks if the subreddit is invalid
    if res.status_code == 200:
        resp = res.json()
        hot_posts = resp.get('data').get('children')
        after = resp.get('data').get('after')

        # Print each hot post title
        for post in hot_posts:
            hot_list.append(post.get('data').get('title'))

        # Get the next page of hot posts
        if after is not None:
            recurse(subreddit, hot_list, after)

        return hot_list
    return None
