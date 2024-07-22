import requests
import json  # Import the json library

url = "https://api.cropmanage.ucanr.edu/Token"
username = "andyboy420019@gmail.com"  
password = "jTiPc7X!hpC2BA"  

payload = {
    'username': username,
    'password': password,
    'grant_type': 'password'
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.post(url, data=payload, headers=headers)

if response.status_code == 200:
    access_token = response.json().get('access_token')
else:
    print("Failed to get access token:", response.text)
    exit()

headers['Authorization'] = f'Bearer {access_token}'

ranch_endpoint = "https://api.cropmanage.ucanr.edu/v2/ranches.json"
response = requests.get(ranch_endpoint, headers=headers)

if response.status_code == 200:
    ranches = response.json()
    print("Ranches:")
    print(json.dumps(ranches, indent=4))  # Pretty-print JSON data
else:
    print("Failed to get ranches data:", response.text)

def get_ranch_details(access_token):
    url = f"https://api.cropmanage.ucanr.edu/v2/ranches/{'dac8275a-edc6-4d82-adc3-f0e398537308'}.json"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code

ranch_guid = 'dac8275a-edc6-4d82-adc3-f0e398537308'
ranch_details = get_ranch_details(access_token)
print("Ranch Details:")
print(json.dumps(ranch_details, indent=4))  # Pretty-print JSON data

def get_ranch_lots(ranch_guid, access_token):
    url = f"https://api.cropmanage.ucanr.edu/v2/ranches/{ranch_guid}/lots.json"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code

# ranch_lots = get_ranch_lots(ranch_guid, access_token)
# print("Ranch Lots Details:")
# print(json.dumps(ranch_lots, indent=4))  # Pretty-print JSON data

def get_ranch_plantings(ranch_guid, access_token):
    url = f"https://api.cropmanage.ucanr.edu/v2/ranches/{ranch_guid}/plantings.json"
    params = {
        'active': True,
        'commodityTypeId': None
    }
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Failed to retrieve plantings: {response.text}"

# ranch_plantings = get_ranch_plantings(ranch_guid, access_token)
# print("Ranch Plantings:")
# print(json.dumps(ranch_plantings, indent=4))  # Pretty-print JSON data

def get_planting_details(planting_id, access_token):
    url = f"https://api.cropmanage.ucanr.edu/v2/plantings/{planting_id}.json"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Failed to retrieve planting details: {response.text}"

planting_id = '15717'
# planting_details = get_planting_details(planting_id, access_token)
# print("Planting Details:")
# print(json.dumps(planting_details, indent=4))  # Pretty-print JSON data

def get_irrigation_event_details(planting_id, access_token):
    url = f"https://api.cropmanage.ucanr.edu/v2/plantings/{planting_id}/irrigation-events/details.json"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Failed to retrieve irrigation event details: {response.text}"

irrigation_details = get_irrigation_event_details(planting_id, access_token)
print("Irrigation Event Details:")
print(json.dumps(irrigation_details, indent=4))  # Pretty-print JSON data