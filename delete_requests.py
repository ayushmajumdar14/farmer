import requests
import os

access_token = os.getenv("ACCESS_TOKEN")
base_url_v2 = os.getenv("BASE_CROP_MANAGE_URL_V2")
base_url_v3 = os.getenv("BASE_CROP_MANAGE_URL_V3")

# (COULD NOT TEST)
# DELETE v2/cut-events/{id}.{ext}
# Deletes a cut event.
def delete_cut_event(access_token, id):
    url = f"{base_url_v2}cut-events/{id}." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.delete(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# DELETE v2/fertilization-events/{id}.{ext}
# Deletes a fertilization event.
def delete_fertilization_event(access_token, id):
    url = f"{base_url_v2}fertilization-events/{id}." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.delete(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# DELETE v2/ranches/{ranchGuid}/fertilizers/{id}.{ext}
# Deletes a fertilizer from a ranch.
def delete_fertilizer(access_token, id, ranchGuid):
    url = f"{base_url_v2}ranches/{ranchGuid}/fertilizers/{id}." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.delete(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# DELETE v2/irrigation-events/{id}.{ext}
# Deletes an irrigation event.
def delete_irrigation_event(access_token, id):
    url = f"{base_url_v2}irrigation-events/{id}." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.delete(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# DELETE v2/plantings/{plantingId}.{ext}
# Deletes a planting.
def delete_planting(access_token, plantingId):
    url = f"{base_url_v2}plantings/{plantingId}." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.delete(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# DELETE v2/ranches/{ranchGuid}.json
# Deletes a ranch.
def delete_ranch(access_token, ranchGuid):
    url = f"{base_url_v2}ranches/{ranchGuid}.json"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.delete(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# DELETE v2/lots/{lotId}.json
# Deletes a planting area from ranch.
def delete_planting_area(access_token, lotId):
    url = f"{base_url_v2}lots/{lotId}.json"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.delete(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# DELETE v2/ranches/{ranchGuid}/wells/{wellId}.json
# Deletes a well from a ranch.
def delete_well(access_token, ranchGuid, wellId):
    url = f"{base_url_v2}ranches/{ranchGuid}/wells/{wellId}.json"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.delete(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# DELETE v2/soil-sample-events/{id}.{ext}
# Delete a soil sample event.
def delete_soil_sample_event(access_token, id):
    url = f"{base_url_v2}soil-sample-events/{id}." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.delete(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# DELETE v2/tissue-sample-events/{id}.{ext}
# Delete tissue sample event.
def delete_tissue_sample_event(access_token, id):
    url = f"{base_url_v2}tissue-sample-events/{id}." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.delete(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# DELETE v2/ranches/{ranchGuid}/users/{userIdTarget}.json
# Remove user from ranch.
def delete_ranch_user(access_token, ranchGuid, userIdTarget):
    url = f"{base_url_v2}ranches/{ranchGuid}/users/{userIdTarget}.json"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.delete(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# DELETE v2/ranches/{ranchGuid}/weather-stations/{stationId}.{ext}
# Delete weather station from ranch.
def delete_weather_station(access_token, stationId, ranchGuid):
    url = f"{base_url_v2}ranches/{ranchGuid}/weather-stations/{stationId}." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.delete(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code