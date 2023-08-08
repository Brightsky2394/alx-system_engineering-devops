#!/usr/bin/python3
"""queries the Reddit API"""
from requests import get


def top_ten(subreddit):
    """prints the titles of the first 10
    hot posts listed for a given subreddit."""
    base_url = 'https://www.reddit.com'
    api_url = "{base}/r/{sub}/hot.json".format(base=base_url, sub=subreddit)
    user_agent = {'user-agent': 'my user agent 1.2'}
    payload = {'limit': '10'}
    response = get(api_url, headers=user_agent, params=payload,
                   allow_redirects=False)
    if response.status_code in [302, 404]:
        print('None')
    else:
        results = response.json()
        data = results.get('data')
        if data and data.get('children'):
            hot_posts = data.get('children')
            for post in hot_posts:
                post_data = post.get('data')
                if post_data and post_data.get('title'):
                    print(post_data.get('title'))
