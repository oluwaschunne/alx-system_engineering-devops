#!/usr/bin/python3
"""Write a function that queries the Reddit
API and returns the number of subscribers"""

import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint for getting subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid API rate-limiting issues
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        data = response.json()
        # Extract the number of subscribers from the JSON response
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # If the subreddit is invalid or doesn't exist, return 0
        return 0
