#!/usr/bin/python3
"""
Function that queries Reddit API and returns the titles
of all hot articles for a given subreddit
"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Request to reddit api and process response"""
    import requests

    resp = requests.get("https://www.reddit.com/r/{}/hot.json"
                        .format(subreddit),
                        params={"count": count, "after": after},
                        headers={"User-Agent": "mozilla"},
                        allow_redirects=False)
    if resp.status_code >= 400:
        return None

    h_list = hot_list + [child.get("data").get("title")
                         for child in resp.json()
                         .get("data")
                         .get("children")]

    info = resp.json()
    if not info.get("data").get("after"):
        return h_list

    return recurse(subreddit, h_list, info.get("data").get("count"),
                   info.get("data").get("after"))
