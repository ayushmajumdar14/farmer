import requests

# (COULD NOT TEST)
# PUT v2/fertilization-events/{id}.{ext}
# Updates a fertilization event.
def put_update_fertilization_event(access_token, id, fertilizationEvent, managerNRecommendation, managerFertilizationAmount, plantingId):
    url = f"https://api.cropmanage.ucanr.edu/v2/fertilization-events/{id}." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    data = {
        "FertilizationEvent": fertilizationEvent,
        "ManagerNRecommendation": managerNRecommendation,
        "ManagerFertilizationAmount": managerFertilizationAmount,
        "PlantingId": plantingId
    }

    # Remove keys with None values
    data = {key: value for key, value in data.items() if value is not None}

    response = requests.put(url, headers=headers, json=data)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# PUT v3/irrigation-events/{id}.{ext}
# Updates an irrigation event.
def put_update_irrigation_event(access_token, id, eventDate, irrigationMethodId, managerAmountRecommendation, managerAmountRecommendationHours, waterApplied, waterAppliedHours, isCustomDeficitEnabled, customDeficit=None):
    url = f"https://api.cropmanage.ucanr.edu/v2/fertilization-events/{id}." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    if (managerAmountRecommendation is None and managerAmountRecommendationHours is not None) or (managerAmountRecommendation is not None and managerAmountRecommendationHours is None):
        raise ValueError("Error: managerAmountRecommendation and managerAmountRecommendationHours not properly defined.")
    
    if (waterApplied is None and waterAppliedHours is not None) or (waterApplied is not None and waterAppliedHours is None):
        raise ValueError("Error: waterApplied and waterAppliedHours not properly defined.")
    
    if customDeficit is not None:
        isCustomDeficitEnabled = True
    else:
        isCustomDeficitEnabled = False

    data = {
        "EventDate": eventDate,
        "IrrigationMethodId": irrigationMethodId,
        "ManagerAmountRecommendation": managerAmountRecommendation,
        "ManagerAmountRecommendationHours": managerAmountRecommendationHours,
        "WaterApplied": waterApplied,
        "WaterAppliedHours": waterAppliedHours,
        "CustomDeficit": customDeficit,
        "IsCustomDeficitEnabled": isCustomDeficitEnabled
    }

    # Remove keys with None values
    data = {key: value for key, value in data.items() if value is not None}

    response = requests.put(url, headers=headers, json=data)
    return response.json() if response.status_code == 200 else response.status_code