#!/usr/bin/python3
"""
Function that queries Reddit API and returns the number of suscribers
"""


def number_of_subscribers(subreddit):
    """Request to the reddit API"""
    import requests

    resp = requests.get("https://www.reddit.com/r/{}/about.json"
                        .format(subreddit),
                        headers={"User-Agent": "Mozilla",
                                 "Content-Type": "application/json"},
                        allow_redirects=False,)
    if resp.status_code >= 300:
        return 0

    return resp.json().get("data").get("subscribers")
