# Program to get the soil moisture data of a specific ranch

import requests
import json

# Function to get the user's access token
def get_access_token():
    url = "https://api.cropmanage.ucanr.edu/Token"
    username = input("Username > ") 
    password = input("Password > ") 

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
        return access_token
    else:
        print("\nFailed to get access token. Reason:", response.json()["error_description"])
        exit()

# Function to get the ranches that the user has access to
def get_ranches(access_token):
    url = "https://api.cropmanage.ucanr.edu/v2/ranches.{ext}"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)
    return response.json()

# Function to get the plantings the user has access to
def get_plantings(ranchGuid, access_token):
    url = f"https://api.cropmanage.ucanr.edu/v2/ranches/{ranchGuid}/plantings." + "{ext}"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    return response.json()

# Function to get the soil moisture data
def get_soil_moisture_data(planting, access_token):
    url = f"https://api.cropmanage.ucanr.edu/v2/plantings/{planting}/soil-moisture-data." + "{ext}"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)
    return response.json()

# Main function
def main():
    # Getting user access token
    at = get_access_token()

    # Getting the ranch that they would like to access
    ranch_list = get_ranches(at)
    ranch = dict()
    ranch_name = input("What ranch would you like to access? > ")
    for item in ranch_list:
        if item["Name"].lower() == ranch_name.lower():
            ranch = item

    if ranch == dict():
        print("Ranch not found! Exiting...")
        exit()
    else:
        print("Ranch found!")

    # Getting the planting that they would like to get the soil moisture data to
    planting_list = get_plantings(ranch["Ranch_External_GUID"], at)
    planting = dict()
    planting_name = input(f"What planting in '{ranch['Name']}' would you like to get the soil moisture data for? > ")
    for item in planting_list:
        if item["Name"].lower() == planting_name.lower():
            planting = item

    if planting == dict():
        print("Planting not found! Exiting...")
        exit()
    else:
        print("Planting found!")
    
    # Accessing the soil moisture data
    soil_moisture_data = get_soil_moisture_data(planting["Id"], at)
    print(f"Here is the planting's soil moisture data:")
    print(json.dumps(soil_moisture_data, indent=4))

if __name__ == "__main__":
    main()