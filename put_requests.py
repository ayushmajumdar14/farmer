import requests
import os

access_token = os.getenv("ACCESS_TOKEN")
base_url_v2 = os.getenv("BASE_CROP_MANAGE_URL_V2")
base_url_v3 = os.getenv("BASE_CROP_MANAGE_URL_V3")

# (COULD NOT TEST)
# PUT v2/fertilization-events/{id}.{ext}
# Updates a fertilization event.
def put_update_fertilization_event(access_token, id, fertilizationEvent, managerNRecommendation, managerFertilizationAmount, plantingId):
    url = f"{base_url_v2}fertilization-events/{id}." + "{ext}"

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
    url = f"{base_url_v3}irrigation-events/{id}." + "{ext}"

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

# (COULD NOT TEST)
# PUT v3/plantings/{plantingId}.json
# Updates a planting.
def put_update_planting(access_token, plantingId, defaultCropTypeId, name, wetDate, harvestDate, lotId, coordinates, acres, irrigationSettings, advancedSettings=None, macroTunnelSettings=None, stressSettings=None, perennialCropSettings=None):
    url = f"{base_url_v3}plantings/{plantingId}.json"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    data = {
        "DefaultCropTypeId": defaultCropTypeId,
        "Name": name,
        "WetDate": wetDate,
        "HarvestDate": harvestDate,
        "LotId": lotId,
        "Coordinates": coordinates,
        "Acres": acres,
        "IrrigationSettings": irrigationSettings,
        "AdvancedSettings": advancedSettings,
        "MacroTunnelSettings": macroTunnelSettings,
        "StressSettings": stressSettings,
        "PerennialCropSettings": perennialCropSettings
    }

    # Remove keys with None values
    data = {key: value for key, value in data.items() if value is not None}

    response = requests.put(url, headers=headers, json=data)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# PUT v3/ranches/{ranchGuid}.json
# Updates ranch information.
def put_update_ranch(access_token, ranchGuid, name, coordinates, acres):
    url = f"{base_url_v3}ranches/{ranchGuid}.json"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    data = {
        "Name": name,
        "Coordinates": coordinates,
        "Acres": acres
    }

    # Remove keys with None values
    data = {key: value for key, value in data.items() if value is not None}

    response = requests.put(url, headers=headers, json=data)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# PUT v3/lots/{id}.json
# Updates a planting area.
def put_update_planting_area(access_token, id, name, acres, coordinates, obstructionDepth):
    url = f"{base_url_v3}lots/{id}.json"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    data = {
        "Name": name,
        "Acres": acres,
        "Coordinates": coordinates,
        "ObstructionDepth": obstructionDepth
    }

    # Remove keys with None values
    data = {key: value for key, value in data.items() if value is not None}

    response = requests.put(url, headers=headers, json=data)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# PUT v2/ranches/{ranchGuid}/wells/{wellId}.json
# Updates a well.
def put_update_well(access_token, ranchGuid, wellId, id, name, electricalConductivity, nitrogenPPM):
    url = f"{base_url_v2}ranches/{ranchGuid}/wells/{wellId}.json"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    data = {
        "Id": id,
        "Name": name,
        "ElectricalConductivity": electricalConductivity,
        "NitrogenPPM": nitrogenPPM
    }

    # Remove keys with None values
    data = {key: value for key, value in data.items() if value is not None}

    response = requests.put(url, headers=headers, json=data)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# PUT v2/soil-sample-events/{id}.{ext}
# Updates a soil sample event.
def put_update_planting_area(access_token, id, eventDate, sampleTypeId, sampleDepth, cropStageId, soilMoistureId, nitrogen, otherNutrients, dateOnly):
    url = f"{base_url_v2}soil-sample-events/{id}." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    data = {
        "Id": id,
        "EventDate": eventDate,
        "SampleTypeId": sampleTypeId,
        "SampleDepth": sampleDepth,
        "CropStageId": cropStageId,
        "SoilMoistureId": soilMoistureId,
        "Nitrogen": nitrogen,
        "OtherNutrients": otherNutrients,
        "DateOnly": dateOnly
    }

    # Remove keys with None values
    data = {key: value for key, value in data.items() if value is not None}

    response = requests.put(url, headers=headers, json=data)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# PUT v3/tissue-sample-events/{eventId}.{ext}
# Update tissue sample event.
def put_tissue_sample_event(access_token, eventId, eventDate, locationId, locationDetails, cropStageId, notes, tissueSampleNutrients):
    url = f"{base_url_v3}tissue-sample-events/{eventId}." + "{ext}"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    data = {
        "EventDate": eventDate,
        "LocationId": locationId,
        "LocationDetails": locationDetails,
        "CropStageId": cropStageId,
        "Notes": notes,
        "TissueSampleNutrients": tissueSampleNutrients
    }

    # Remove keys with None values
    data = {key: value for key, value in data.items() if value is not None}

    response = requests.put(url, headers=headers, json=data)
    return response.json() if response.status_code == 200 else response.status_code