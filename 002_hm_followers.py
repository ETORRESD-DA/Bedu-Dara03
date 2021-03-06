from datetime import datetime
import requests
import json

# CONSTANTS
URL_BASE='https://api.github.com/'

# FUNTIONS
def get_github_user(username):
    url = f'{URL_BASE}users/{username}'
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    print("Sin conexion ",response.status_code)
    return None

def download_followers(followers_url):
    response = requests.get(followers_url)
    if response.status_code == 200:
        response_content = response.content
        filename = f'tmp/base.json'
        with open(filename, 'wb') as json:
            json.write(response_content)
            return filename
    return None

def download_user_avatar(image_url,login):
    response = requests.get(image_url,login)
    if response.status_code == 200:
        response_content = response.content
        filename = f'tmp/{image_filename()}{login}.png'
        with open(filename, 'wb') as image:
            image.write(response_content)
            return filename
    return None


def image_filename():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    return timestamp

user = get_github_user("galileoguzman")

if user:
    user_followers_url = user.get("followers_url")
    download_followers(user_followers_url)
    f = open("tmp/base.json", "r")
    content = f.read()
    jsondecoded = json.loads(content)
    for elemento in jsondecoded:
        follower=get_github_user (elemento['login'])   
        user_avatar_url = follower.get('avatar_url')
        user_avatar_name=follower.get('login')
        download_user_avatar(user_avatar_url,user_avatar_name)
else:
    print('User not found')



