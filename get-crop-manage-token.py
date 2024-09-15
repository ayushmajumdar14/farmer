import json
import requests

from dotenv import load_dotenv, set_key, find_dotenv

# Loading The .env File
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Function To Get The Access Token From CropManage  
def get_crop_manage_token(username, password):
    form_data = {
        'username': username,
        'password': password,
        'grant_type': 'password'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    url = 'https://api.cropmanage.ucanr.edu/Token'
    response = requests.post(url, data=form_data, headers=headers)
    
    res = response.text
    try:
        response = json.loads(res)
    except Exception as e:   
        response = res

    if ('access_token' in response):
        return response['access_token']
    return None

# Main Program To Get CropManage Access Token
if __name__ == '__main__':
 
    while True:
        
        username = input("Enter username: ")
        password = input("Enter password: ")

        access_token = get_crop_manage_token(username, password)
        if (access_token):
            print('My CropManage Token:', access_token)
            print('updating .env file setting CROP-MANAGE-TOKEN')
            set_key(dotenv_path, 'ACCESS_TOKEN', access_token)
            break
        else:
            print("Invalid username and/or password!")