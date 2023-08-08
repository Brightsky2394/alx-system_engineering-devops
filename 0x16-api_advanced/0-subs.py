#!/usr/bin/python3
""" queries the Reddit API """
from requests import get


def number_of_subscribers(subreddit):
    """ returns the number of subscribers
    (not active users, total subscribers)
    for a given subreddit """
    base_url = "https://www.reddit.com"
    api_url = "{base}/r/{sub}/about.json".format(base=base_url, sub=subreddit)
    user_agent = {'user-agent': 'My user agent 1.2'}
    response = get(api_url, headers=user_agent, allow_redirects=False)
    if response.status_code in [302, 404]:
        return 0
    return response.json().get('data').get('subscribers')
