import requests

#!/usr/bin/python3

def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return
    
    try:
        data = response.json().get('data', {}).get('children', [])
        if not data:
            print(None)
            return
        
        for post in data:
            print(post.get('data', {}).get('title'))
    except Exception:
        print(None)