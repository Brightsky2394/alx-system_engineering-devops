#!/usr/bin/python3
"""queries the Reddit API"""
from requests import get


def recurse(subreddit, hot_list=[]):
    """returns a list containing the titles
    of all hot articles for a given subreddit"""

    base_url = 'https://www.reddit.com'
    api_url = '{base}/r/{sub}/hot.json'.format(base=base_url, sub=subreddit)
    user_agent = {'user-agent': 'my user agent 1.2'}
    payload = {'after': after, 'limit': 100}
    response = get(api_url, headers=user_agent, params=payload,
                   allow_redirects=False)
    if response.status_code == 200:
        results = response.json()
        data = results.get('data')
        hot_posts = data.get('children')
        for post in hot_posts:
            post_data = post.get('data')
            hot_list.append(post_data.get('title'))
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    return None
