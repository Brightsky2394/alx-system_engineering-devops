#!/usr/bin/python3
""" recursive function that queries the Reddit API """
import requests
import sys
after = None


def recurse(subreddit, hot_list=[]):
    """     Args:
        subreddit: subreddit name
        hot_list: list of hot titles in subreddit
        after: last hot_item appended to hot_list
    Returns:
        a list containing the titles of all hot articles for the subreddit
        or None if queried subreddit is invalid """
    global after
    user_agent = {'user-agent': 'my user agent 1.2'}
    base_url = "https://www.reddit.com"
    api_url = "{base}/r/{sub}/hot.json".format(base=base_url, sub=subreddit)
    parameters = {'after': after}
    response = requests.get(api_url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        next_ = response.json().get('data').get('after')
        if next_ is not None:
            after = next_
            recurse(subreddit, hot_list)
        list_titles = response.json().get('data').get('children')
        for title_ in list_titles:
            hot_list.append(title_.get('data').get('title'))
        return hot_list
    else:
        return (None)
