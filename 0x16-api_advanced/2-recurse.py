#!/usr/bin/python3
""" Recurse it! """
from requests import get

base_url = "https://www.reddit.com/"
user_agent = {'user-agent': 'my-app/0.0.1'}


def recurse(subreddit, hot_list=[], after=""):
    """
    Returns a list containing the titles of all hot articles for a given
    subreddit. If no results are found for the given subreddit, the function
    should return None.
    """
    if after is None:
        return hot_list

    api_url = "{base}/r/{sub}/hot/.json".format(base=base_url, sub=subreddit)

    params = {
        'limit': 100,
        'after': after
    }

    res = get(url, headers=user_agent, params=params, allow_redirects=False)

    if res.status_code != 200:
        return None

    try:
        js = res.json()

    except ValueError:
        return None

    try:

        data = js.get("data")
        after = data.get("after")
        children = data.get("children")
        for child in children:
            post = child.get("data")
            hot_list.append(post.get("title"))

    except Exception:
        return None

    return recurse(subreddit, hot_list, after)
