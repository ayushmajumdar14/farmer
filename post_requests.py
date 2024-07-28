import requests

# POST v2/ranches/{ranchGuid}/commodity-types.{ext}
# Saves a commodity type ranch association. This association determines what commodity types are available for a ranch.
def post_save_commodity_ranch_association(access_token, ranchGuid, commodityTypeId, cropTypeIds):
    url = f"https://api.cropmanage.ucanr.edu/v2/ranches/{ranchGuid}/commodity-types." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    data = {
        "CommodityTypeId": commodityTypeId,
        "CropTypeIds": cropTypeIds
    }

    # Remove keys with None values
    data = {key: value for key, value in data.items() if value is not None}

    response = requests.post(url, headers=headers, json=data)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# POST v2/cut-events.{ext}
# Creates or updates a cut event.
def post_cut_event(access_token, plantingId, eventDate, maturityId, yieldId, isBookmark, id, dateOnly):
    url = f"https://api.cropmanage.ucanr.edu/v2/cut-events." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    data = {
        "PlantingId": plantingId,
        "EventDate": eventDate,
        "MaturityId": maturityId,
        "Yield": yieldId,
        "IsBookmark": isBookmark,
        "Id": id,
        "DateOnly": dateOnly
    }

    # Remove keys with None values
    data = {key: value for key, value in data.items() if value is not None}

    response = requests.post(url, headers=headers, json=data)
    return response.json() if response.status_code == 200 else response.status_code    

# (COULD NOT TEST)
# POST v2/et-weather-events.{ext}
# Saves an ET weather event.
def post_et_event(access_token, id, et):
    url = f"https://api.cropmanage.ucanr.edu/v2/et-weather-events." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    data = {
        "Id": id,
        "ET": et
    }

    # Remove keys with None values
    data = {key: value for key, value in data.items() if value is not None}

    response = requests.post(url, headers=headers, json=data)
    return response.json() if response.status_code == 200 else response.status_code

# POST v2/fertilization-recommendation.{ext}
# Single call API endpoint for fertilization recommendation.
def post_fertilization_recommendation(access_token, cropTypeId, wetDate, harvestDate, obstructionDepth, eventDate, daysToNextFertilization, fertilizationsPerMonth, ageOfCrop, soilLayers, soilSampleEvents):
    url = f"https://api.cropmanage.ucanr.edu/v2/fertilization-recommendation." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    data = {
        "CropTypeId": cropTypeId,
        "WetDate": wetDate,
        "HarvestDate": harvestDate,
        "ObstructionDepth": obstructionDepth,
        "EventDate": eventDate,
        "DaysToNextFertilization": daysToNextFertilization,
        "FertilizationsPerMonth": fertilizationsPerMonth,
        "AgeOfCrop": ageOfCrop,
        "SoilLayers": soilLayers,
        "SoilSampleEvents": soilSampleEvents
    }

    # Remove keys with None values
    data = {key: value for key, value in data.items() if value is not None}

    response = requests.post(url, headers=headers, json=data)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# POST v2/plantings/{plantingId}/fertilization-events.{ext}
# Creates a new fertilization event.
def post_fertilization_event(access_token, plantingId, daysToNextFertilization, fertilizationsPerMonth, eventDate, cropStageId, soilSampleEventDate, fertilizerId):
    url = f"https://api.cropmanage.ucanr.edu/v2/plantings/{plantingId}/fertilization-events." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    data = {
        "DaysToNextFertilization": daysToNextFertilization,
        "FertilizationsPerMonth": fertilizationsPerMonth,
        "EventDate": eventDate,
        "CropStageId": cropStageId,
        "SoilSampleEventDate": soilSampleEventDate,
        "FertilizerId": fertilizerId
    }

    # Remove keys with None values
    data = {key: value for key, value in data.items() if value is not None}

    response = requests.post(url, headers=headers, json=data)
    return response.json() if response.status_code == 200 else response.status_code

# POST v2/ranches/{ranchGuid}/fertilizers/{fertilizerId}.{ext}
# Add a fertilizer to a ranch.
def post_cut_event(access_token, ranchGuid, fertilizerId):
    url = f"https://api.cropmanage.ucanr.edu/v2/ranches/{ranchGuid}/fertilizers/{fertilizerId}." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.post(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# POST v2/irrigation-recommendation.{ext}
# Single call Web API endpoint for irrigation recommendations. This Web API call can be used to request irrigation recommendations from CropManage, without having to first set up ranches or plantings.
def post_irrigation_recommendation(access_token, eventDate, cropTypeId, wetDate, harvestDate, weatherStationId, irrigationEvents, soilProperties, latitude, longitude, distributionUniformity=85, leechingRequirement=0, ageOfCrop=None, cropSensitivity=1, cutEvents=None, macroTunnelStart=None, macroTunnelEnd=None, stress=None):
    url = f"https://api.cropmanage.ucanr.edu/v2/irrigation-recommendation." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    data = {
        "EventDate": eventDate,
        "DistributionUniformity": distributionUniformity,
        "CropTypeId": cropTypeId,
        "WetDate": wetDate,
        "HarvestDate": harvestDate,
        "WeatherStationId": weatherStationId,
        "IrrigationEvents": irrigationEvents,
        "SoilProperties": soilProperties,
        "CutEvents": cutEvents,
        "LeechingRequirement": leechingRequirement,
        "AgeOfCrop": ageOfCrop,
        "CropSensitivity": cropSensitivity,
        "MacroTunnelStart": macroTunnelStart,
        "MacroTunnelEnd": macroTunnelEnd,
        "Stress": stress,
        "Latitude": latitude,
        "Longitude": longitude
    }

    # Remove keys with None values
    data = {key: value for key, value in data.items() if value is not None}

    response = requests.post(url, headers=headers, json=data)
    return response.json() if response.status_code == 200 else response.status_code

# POST v2/season-et.{ext}
# Endpoint for the public ET calculator.
def post_season_et(access_token, eventDate, cropTypeId, wetDate, harvestDate, weatherStationId, irrigationEvents, soilProperties, latitude, longitude, distributionUniformity=85, leechingRequirement=0, ageOfCrop=None, cropSensitivity=1, cutEvents=None, macroTunnelStart=None, macroTunnelEnd=None, stress=None):
    url = f"https://api.cropmanage.ucanr.edu/v2/season-et." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    data = {
        "EventDate": eventDate,
        "DistributionUniformity": distributionUniformity,
        "CropTypeId": cropTypeId,
        "WetDate": wetDate,
        "HarvestDate": harvestDate,
        "WeatherStationId": weatherStationId,
        "IrrigationEvents": irrigationEvents,
        "SoilProperties": soilProperties,
        "CutEvents": cutEvents,
        "LeechingRequirement": leechingRequirement,
        "AgeOfCrop": ageOfCrop,
        "CropSensitivity": cropSensitivity,
        "MacroTunnelStart": macroTunnelStart,
        "MacroTunnelEnd": macroTunnelEnd,
        "Stress": stress,
        "Latitude": latitude,
        "Longitude": longitude
    }

    # Remove keys with None values
    data = {key: value for key, value in data.items() if value is not None}

# (COULD NOT TEST)
# POST v3/plantings/{plantingId}/irrigation-events.{ext}
# Creates an irrigation event.
def post_irrigation_event(access_token, plantingId, eventDate, irrigationMethodId, customDeficit, isCustomDeficitEnabled, managerAmountRecommendation=None, managerAmountRecommendationHours=None, waterApplied=None, waterAppliedHours=None):
    url = f"https://api.cropmanage.ucanr.edu/v3/plantings/{plantingId}/irrigation-events." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    if (managerAmountRecommendation is None and managerAmountRecommendationHours is not None) or (managerAmountRecommendation is not None and managerAmountRecommendationHours is None):
        raise ValueError("Error: managerAmountRecommendation and managerAmountRecommendationHours not properly defined.")
    
    if (waterApplied is None and waterAppliedHours is not None) or (waterApplied is not None and waterAppliedHours is None):
        raise ValueError("Error: waterApplied and waterAppliedHours not properly defined.")

    data = {
        "EventDate": None,
        "IrrigationMethodId": None,
        "ManagerAmountRecommendation": None,
        "ManagerAmountRecommendationHours": None,
        "WaterApplied": None,
        "WaterAppliedHours": None,
        "CustomDeficit": None,
        "IsCustomDeficitEnabled": None
    }

    # Remove keys with None values
    data = {key: value for key, value in data.items() if value is not None}

    response = requests.post(url, headers=headers, json=data)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# POST v3/ranches/{ranchGuid}/plantings.json
# Creates a new planting.
def post_planting(access_token, ranchGuid, defaultCropTypeId, name, wetdate, harvestDate, lotId, coordinates, acres, irrigationSettings, advancedSettings=None, macroTunnelSettings=None, stressSettings=None, perennialCropSettings=None):
    url = f"https://api.cropmanage.ucanr.edu/v3/ranches/{ranchGuid}/plantings.json"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    data = {
        "DefaultCropTypeId": None,
        "Name": None,
        "WetDate": None,
        "HarvestDate": None,
        "LotId": None,
        "Coordinates": None,
        "Acres": None,
        "IrrigationSettings": None,
        "AdvancedSettings": None,
        "MacroTunnelSettings": None,
        "StressSettings": None,
        "PerennialCropSettings": None
    }   

    # Remove keys with None values
    data = {key: value for key, value in data.items() if value is not None}

    response = requests.post(url, headers=headers, json=data)
    return response.json() if response.status_code == 200 else response.status_code



# Function to get the user's access token
def get_access_token():
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
        return access_token
    else:
        print("\nFailed to get access token. Reason:", response.json()["error_description"])
        exit()

def main():
    at = get_access_token()
    print(post_save_commodity_ranch_association(at, "dac8275a-edc6-4d82-adc3-f0e398537308", 1, [23, 3716]))

if __name__ == "__main__":
    main()