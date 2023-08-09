#!/usr/bin/python3
""" queries the Reddit API, """
from requests import get

base_url = "https://www.reddit.com/"
user_agent = {'user-agent': 'my user agent 1.3'}


def count_words(subreddit, word_list, after="", word_dic={}):
    """
    Returns a list containing the titles of all hot articles for a
    given subreddit. If no results are found for the given subreddit,
    the function should return None.
    """
    if not word_dic:
        for word in word_list:
            word_dic[word] = 0

    if after is None:
        word_list = [[key, value] for key, value in word_dic.items()]
        word_list = sorted(word_list, key=lambda x: (-x[1], x[0]))
        for w in word_list:
            if w[1]:
                print("{}: {}".format(w[0].lower(), w[1]))
        return None

    url = base_url + "r/{}/hot/.json".format(subreddit)

    payload = {
        'limit': 100,
        'after': after
    }

    res = get(url, headers=user_agent, params=payload, allow_redirects=False)

    if res.status_code != 200:
        return None

    try:
        resp = res.json()

    except ValueError:
        return None

    try:

        data = resp.get("data")
        after = data.get("after")
        children = data.get("children")
        for child in children:
            post = child.get("data")
            title = post.get("title")
            lower = [s.lower() for s in title.split(' ')]

            for w in word_list:
                word_dic[w] += lower.count(w.lower())

    except Exception:
        return None

    count_words(subreddit, word_list, after, word_dic)