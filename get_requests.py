import requests

# GET v2/commodity-types.json
# Returns a complete list of commodity types in CropManage.
def get_commodity_types(access_token):
    url = "https://api.cropmanage.ucanr.edu/v2/commodity-types.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/crop-stages.json?commodityTypeId={commodityTypeId}
# Returns a list of crop stages associated with a commodity type.
def get_crop_stages(access_token, commodityTypeId=0):
    url = f"https://api.cropmanage.ucanr.edu/v2/crop-stages.json?commodityTypeId={commodityTypeId}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/crop-types.{ext}?includePrevious={includePrevious}&commodityTypeId={commodityTypeId}
# Returns a list of all crop types in the system.
def get_crop_types(access_token, includePrevious=False, commodityTypeId=None):
    url = f"https://api.cropmanage.ucanr.edu/v2/crop-types." + "{ext}" + f"?includePrevious={includePrevious}&commodityTypeId={commodityTypeId}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/crop-types/{cropTypeId}.{ext}
# Get crop type data, based on ID.
def get_crop_type_by_id(access_token, cropTypeId):
    url = f"https://api.cropmanage.ucanr.edu/v2/crop-types/{cropTypeId}." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{ranchGuid}/commodity-types/{commodityTypeId}/crop-types.{ext}?shouldFilterUnassociated={shouldFilterUnassociated}
# Returns a list of crop types associated with a ranch. Normally, a ranch is only associated with a handful of commodity types and a select number of crop types.
def get_crop_types_of_ranch(access_token, ranchGuid, commodityTypeId, shouldFilterUnassociated=True):
    url = f"https://api.cropmanage.ucanr.edu/v2/ranches/{ranchGuid}/commodity-types/{commodityTypeId}/crop-types." + "{ext}" + f"?shouldFilterUnassociated={shouldFilterUnassociated}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# GET v2/cut-events/{id}.{ext}
# Returns cut event data.
def get_cut_event_data(access_token, id):
    url = f"https://api.cropmanage.ucanr.edu/v2/cut-events/{id}." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (ADDED 201 STATUS CODE)
# GET v2/plantings/{plantingId}/et-weather-events.json
# Returns a list of ET data associated with a planting.
def get_et_weather_events(access_token, planting_id):
    url = f"https://api.cropmanage.ucanr.edu/v2/plantings/{planting_id}/et-weather-events.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if (response.status_code == 200 or response.status_code == 201) else response.status_code

# GET v2/fertilization-events/{id}.{ext}
# Returns a fertilization event.
def get_fertilization_event(access_token, event_id):
    url = f"https://api.cropmanage.ucanr.edu/v2/fertilization-events/{event_id}." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# GET v2/fertilization-events/{id}/recommendation.{ext}?soilSampleEventDate={soilSampleEventDate}&daysToNextFertilization={daysToNextFertilization}&fertilizationsPerMonth={fertilizationsPerMonth}&eventDate={eventDate}&nInWater={nInWater}
# Get CropManage recommendation for a fertilizer event.
def get_fertilizer_recommendation(access_token, id, soilSampleEventDate, daysToNextFertilization, fertilizationsPerMonth, eventDate, nInWater):
    url = f"https://api.cropmanage.ucanr.edu/v2/fertilization-events/{id}/recommendation." + "{ext}" + f"?soilSampleEventDate={soilSampleEventDate}&daysToNextFertilization={daysToNextFertilization}&fertilizationsPerMonth={fertilizationsPerMonth}&eventDate={eventDate}&nInWater={nInWater}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/fertilization-events/{eventId}/wells.{ext}
# Returns a list of wells associated with a fertilization event.
def get_fertilization_event_wells(access_token, event_id):
    url = f"https://api.cropmanage.ucanr.edu/v2/fertilization-events/{event_id}/wells." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/fertilization-event-wells/{Id}.{ext}
# Returns a well associated with a fertilization event.
def get_fertilization_event_well(access_token, id):
    url = f"https://api.cropmanage.ucanr.edu/v2/fertilization-event-wells/{id}." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{ranchGuid}/fertilizers.{ext}
# Returns a list of fertilizers associated with a ranch.
def get_fertilizers(access_token, ranch_guid):
    url = f"https://api.cropmanage.ucanr.edu/v2/ranches/{ranch_guid}/fertilizers." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{ranchGuid}/fertilizers/available.{ext}
# Returns a list of fertilizers that are not associated with the ranch but is available for use.
def get_available_fertilizers(access_token, ranch_guid):
    url = f"https://api.cropmanage.ucanr.edu/v2/ranches/{ranch_guid}/fertilizers/available." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/irrigation-events/{id}.{ext}
# Returns an irrigation event.
def get_irrigation_event(access_token, event_id):
    url = f"https://api.cropmanage.ucanr.edu/v2/irrigation-events/{event_id}." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/irrigation-events/{id}/recommendations-interval-summary.{ext}
# Returns CropManage irrigation interval recommendation for a specific irrigation event.
def get_cropmanage_irrigation_recommendation(access_token, id):
    url = f"https://api.cropmanage.ucanr.edu/v2/irrigation-events/{id}/recommendations-interval-summary." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (ONLY ACCESSIBLE FROM CROPMANAGE APPLICATION)
# GET v2/plantings/{plantingId}/irrigation-events/count-events-on-date.{ext}?targetDate={targetDate}
# Endpoint used to check whether an irrigation event already exists on a specific date, to prevent multiple irrigation events from being created on the same date.
def get_irrigation_event_exists(access_token, plantingId, targetDate):
    url = f"https://api.cropmanage.ucanr.edu/v2/plantings/{plantingId}/irrigation-events/count-events-on-date." + "{ext}" f"?targetDate={targetDate}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/plantings/{plantingId}/irrigation-events/details.{ext}
# Returns detailed irrigation data for a planting, including reference ET, canopy cover, average canopy.
def get_irrigation_data(access_token, plantingId):
    url = f"https://api.cropmanage.ucanr.edu/v2/plantings/{plantingId}/irrigation-events/details." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/plantings/{plantingId}/irrigation-events/recommendation-summary.{ext}?eventDate={eventDate}&irrigationMethodId={irrigationMethodId}&eventId={eventId}&customDeficit={customDeficit}
# Get an irrigation recommendation depending on various inputs, including event date and irrigation method.
def get_custom_irrigation_recommendation(access_token, plantingId, eventDate, irrigationMethodId, eventId=None, customDeficit=None):
    url = f"https://api.cropmanage.ucanr.edu/v2/plantings/{plantingId}/irrigation-events/recommendation-summary." + "{ext}" + f"?eventDate={eventDate}&irrigationMethodId={irrigationMethodId}&eventId={eventId}&customDeficit={customDeficit}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# GET v2/plantings/{plantingId}/wells.{ext}
# Returns a list of wells associated with a planting.
def get_wells(access_token, plantingId):
    url = f"https://api.cropmanage.ucanr.edu/v2/plantings/{plantingId}/wells." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/maturities.{ext}
# Returns a list of maturities, used primarily for Alfalfa.
def get_maturities(access_token):
    url = "https://api.cropmanage.ucanr.edu/v2/maturities." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/microsprinklers.{ext}
# Returns a list of micro sprinklers.
def get_microsprinklers(access_token):
    url = "https://api.cropmanage.ucanr.edu/v2/microsprinklers." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/plantings/{id}.{ext}
# Returns planting details.
def get_planting_details(access_token, planting_id):
    url = f"https://api.cropmanage.ucanr.edu/v2/plantings/{planting_id}." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/plantings/{plantingId}/events.{ext}
# Returns events from a specific planting.
def get_planting_events(access_token, plantingId):
    url = f"https://api.cropmanage.ucanr.edu/v2/plantings/{plantingId}/events." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/plantings/{plantingId}/rainfall.{ext}
# Returns rainfall data.
def get_planting_rainfall(access_token, plantingId):
    url = f"https://api.cropmanage.ucanr.edu/v2/plantings/{plantingId}/rainfall." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/plantings/{plantingId}/totals/applied-water.json?startDate={startDate}&endDate={endDate}
# Given planting ID, start and end dates, return total applied water.
def get_total_applied_water(access_token, plantingId, startDate, endDate):
    url = f"https://api.cropmanage.ucanr.edu/v2/plantings/{plantingId}/totals/applied-water.json?startDate={startDate}&endDate={endDate}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{ranchGuid}/plantings.{ext}?active={active}&commodityTypeId={commodityTypeId}
# Returns a list of plantings from a specific ranch. The list can be filtered to only return active plantings or plantings associated with a specific commodity type.
def get_ranch_plantings(access_token, ranchGuid, active=True, commodityTypeId=None):
    url = f"https://api.cropmanage.ucanr.edu/v2/ranches/{ranchGuid}/plantings." + "{ext}" + f"?active={active}&commodityTypeId={commodityTypeId}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches.{ext}
# Returns a list of ranches that the user has access to.
def get_ranches(access_token):
    url = "https://api.cropmanage.ucanr.edu/v2/ranches." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{ranchGuid}.json
# Returns basic ranch information.
def get_ranch_details(access_token, ranch_guid):
    url = f"https://api.cropmanage.ucanr.edu/v2/ranches/{ranch_guid}.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{ranchGuid}/permissions.{ext}
# Retrieves a user's ranch planting permissions.
def get_ranch_planting_permissions(access_token, ranchGuid):
    url = f"https://api.cropmanage.ucanr.edu/v2/ranches/{ranchGuid}/permissions." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{ranchGuid}/users/{userId}/permissions.json
# Returns a user's ranch permissions.
def get_ranch_permissions(access_token, ranchGuid, userId):
    url = f"https://api.cropmanage.ucanr.edu/v2/ranches/{ranchGuid}/users/{userId}/permissions.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/lots/{lotId}.json
# Returns planting area details.
def get_planting_area_details(access_token, lotId):
    url = f"https://api.cropmanage.ucanr.edu/v2/lots/{lotId}.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{ranchGuid}/lots.json
# Returns a list of planting areas associated with a ranch.
def get_planting_areas(access_token, ranchGuid):
    url = f"https://api.cropmanage.ucanr.edu/v2/ranches/{ranchGuid}/lots.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{id}/ranch-wells.{ext}
# Returns a list of wells associated with a ranch.
def get_wells(access_token, id):
    url = f"https://api.cropmanage.ucanr.edu/v2/ranches/{id}/ranch-wells." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/wells/{wellId}.json
# Returns well details.
def get_well_details(access_token, wellId):
    url = f"https://api.cropmanage.ucanr.edu/v2/wells/{wellId}.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/regions.{ext}
# Returns a list of regions in CropManage. Current regions are in California and Hawaii.
def get_regions(access_token):
    url = f"https://api.cropmanage.ucanr.edu/v2/regions." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# GET v2/plantings/{plantingId}/soil-moisture-data.{ext}
# Returns soil moisture data for a planting.
def get_soil_moisture_data(access_token, plantingId):
    url = f"https://api.cropmanage.ucanr.edu/v2/plantings/{plantingId}/soil-moisture-data." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/soil-types.{ext}
# Returns a list of all soil types in the database. This is a simple list of soil types. To retrieve soil types in more detail, call /soil-types/list.{ext}
def get_soil_types(access_token):
    url = f"https://api.cropmanage.ucanr.edu/v2/soil-types." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# GET v2/soil-web.{ext}?lat={lat}&lng={lng}
# A simple call that retrieves soil web data, given coordinates. This call is intended to be used with single call web API which requires soil properties. Warning: This is restricted to registered 3rd party applications to prevent abuse.
def get_soil_data(access_token, lat, lng):
    url = f"https://api.cropmanage.ucanr.edu/v2/soil-web." + "{ext}" + f"?lat={lat}&lng={lng}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/tissue-sample-events/{id}.{ext}
# Returns tissue sample event details.
def get_tissue_sample_event_details(access_token, id):
    url = f"https://api.cropmanage.ucanr.edu/v2/tissue-sample-events/{id}." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/tissue-sample-locations.{ext}
# Returns a list of tissue sample locations.
def get_tissue_sample_locations(access_token):
    url = f"https://api.cropmanage.ucanr.edu/v2/tissue-sample-locations." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/tissue-sample-nutrients.{ext}
# Returns a list of tissue sample nutrients.
def get_tissue_sample_nutrients(access_token):
    url = f"https://api.cropmanage.ucanr.edu/v2/tissue-sample-nutrients." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/user-detail.{ext}
# Get current logged in user's information.
def get_user_details(access_token):
    url = "https://api.cropmanage.ucanr.edu/v2/user-detail." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{ranchGuid}/users.json
# Get users associated with a ranch.
def get_associated_users(access_token, ranchGuid):
    url = f"https://api.cropmanage.ucanr.edu/v2/ranches/{ranchGuid}/users.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/weatherapis.{ext}
# This controller is used to access Weather service records, like CIMIS, and HoboLink.
def get_weather_service_records(access_token):
    url = "https://api.cropmanage.ucanr.edu/v2/weatherapis." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{ranchGuid}/weather-stations.{ext}
# Returns weather stations associated with a ranch.
def get_weather_stations_by_ranch(access_token, ranch_guid):
    url = f"https://api.cropmanage.ucanr.edu/v2/ranches/{ranch_guid}/weather-stations." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/weather-stations.{ext}?activeOnly={activeOnly}&ranchGuid={ranchGuid}&suppressZeroET={suppressZeroET}
# Returns all weather stations in the database.
def get_all_weather_stations(access_token, active_only=False, ranch_guid=None, suppress_zero_et=False):
    url = f"https://api.cropmanage.ucanr.edu/v2/weather-stations.json?activeOnly={active_only}&ranchGuid={ranch_guid}&suppressZeroET={suppress_zero_et}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# GET v2/weather-stations/{id}.{ext}?ranchGuid={ranchGuid}
# Get details for a specific weather station.
def get_weather_station_details(access_token, id, ranchGuid=None):
    url = f"https://api.cropmanage.ucanr.edu/v2/weather-stations/{id}." + "{ext}" + f"?ranchGuid={ranchGuid}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/weather-stations/{stationId}/missingRecords.json
# Get missing station records for a weather station.
def get_missing_station_records(access_token, stationId):
    url = f"https://api.cropmanage.ucanr.edu/v2/weather-stations/{stationId}/missingRecords.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (TESTING PURPOSES)
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