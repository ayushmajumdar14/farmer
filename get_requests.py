import requests
import os

access_token = os.getenv("ACCESS_TOKEN")
base_url_v2 = os.getenv("BASE_CROP_MANAGE_URL_V2")
base_url_v3 = os.getenv("BASE_CROP_MANAGE_URL_V3")

# GET v2/commodity-types.json
# Returns a complete list of commodity types in CropManage.
def get_commodity_types():
    url = f"{base_url_v2}commodity-types.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/crop-stages.json?commodityTypeId={commodityTypeId}
# Returns a list of crop stages associated with a commodity type.
def get_crop_stages(commodityTypeId=0):
    url = f"{base_url_v2}crop-stages.json?commodityTypeId={commodityTypeId}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/crop-types.{ext}?includePrevious={includePrevious}&commodityTypeId={commodityTypeId}
# Returns a list of all crop types in the system.
def get_crop_types(includePrevious=False, commodityTypeId=None):
    url = f"{base_url_v2}crop-types." + "{ext}" + f"?includePrevious={includePrevious}&commodityTypeId={commodityTypeId}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/crop-types/{cropTypeId}.{ext}
# Get crop type data, based on ID.
def get_crop_type_by_id(cropTypeId):
    url = f"{base_url_v2}crop-types/{cropTypeId}." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{ranchGuid}/commodity-types/{commodityTypeId}/crop-types.{ext}?shouldFilterUnassociated={shouldFilterUnassociated}
# Returns a list of crop types associated with a ranch. Normally, a ranch is only associated with a handful of commodity types and a select number of crop types.
def get_crop_types_of_ranch(ranchGuid, commodityTypeId, shouldFilterUnassociated=True):
    url = f"{base_url_v2}ranches/{ranchGuid}/commodity-types/{commodityTypeId}/crop-types." + "{ext}" + f"?shouldFilterUnassociated={shouldFilterUnassociated}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# GET v2/cut-events/{id}.{ext}
# Returns cut event data.
def get_cut_event_data(id):
    url = f"{base_url_v2}cut-events/{id}." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/plantings/{plantingId}/et-weather-events.json
# Returns a list of ET data associated with a planting.
def get_et_weather_events(planting_id):
    url = f"{base_url_v2}plantings/{planting_id}/et-weather-events.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if (response.status_code == 200 or response.status_code == 201) else response.status_code

# GET v2/fertilization-events/{id}.{ext}
# Returns a fertilization event.
def get_fertilization_event(event_id):
    url = f"{base_url_v2}fertilization-events/{event_id}." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# GET v2/fertilization-events/{id}/recommendation.{ext}?soilSampleEventDate={soilSampleEventDate}&daysToNextFertilization={daysToNextFertilization}&fertilizationsPerMonth={fertilizationsPerMonth}&eventDate={eventDate}&nInWater={nInWater}
# Get CropManage recommendation for a fertilizer event.
def get_fertilizer_recommendation(id, soilSampleEventDate, daysToNextFertilization, fertilizationsPerMonth, eventDate, nInWater):
    url = f"{base_url_v2}fertilization-events/{id}/recommendation." + "{ext}" + f"?soilSampleEventDate={soilSampleEventDate}&daysToNextFertilization={daysToNextFertilization}&fertilizationsPerMonth={fertilizationsPerMonth}&eventDate={eventDate}&nInWater={nInWater}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/fertilization-events/{eventId}/wells.{ext}
# Returns a list of wells associated with a fertilization event.
def get_fertilization_event_wells(event_id):
    url = f"{base_url_v2}fertilization-events/{event_id}/wells." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/fertilization-event-wells/{Id}.{ext}
# Returns a well associated with a fertilization event.
def get_fertilization_event_well(id):
    url = f"{base_url_v2}fertilization-event-wells/{id}." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{ranchGuid}/fertilizers.{ext}
# Returns a list of fertilizers associated with a ranch.
def get_fertilizers(ranch_guid):
    url = f"{base_url_v2}ranches/{ranch_guid}/fertilizers." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{ranchGuid}/fertilizers/available.{ext}
# Returns a list of fertilizers that are not associated with the ranch but is available for use.
def get_available_fertilizers(ranch_guid):
    url = f"{base_url_v2}ranches/{ranch_guid}/fertilizers/available." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/irrigation-events/{id}.{ext}
# Returns an irrigation event.
def get_irrigation_event(event_id):
    url = f"{base_url_v2}irrigation-events/{event_id}." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/irrigation-events/{id}/recommendations-interval-summary.{ext}
# Returns CropManage irrigation interval recommendation for a specific irrigation event.
def get_cropmanage_irrigation_recommendation(id):
    url = f"{base_url_v2}irrigation-events/{id}/recommendations-interval-summary." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# GET v2/plantings/{plantingId}/irrigation-events/count-events-on-date.{ext}?targetDate={targetDate}
# Endpoint used to check whether an irrigation event already exists on a specific date, to prevent multiple irrigation events from being created on the same date.
def get_irrigation_event_exists(plantingId, targetDate):
    url = f"{base_url_v2}plantings/{plantingId}/irrigation-events/count-events-on-date." + "{ext}" f"?targetDate={targetDate}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/plantings/{plantingId}/irrigation-events/details.{ext}
# Returns detailed irrigation data for a planting, including reference ET, canopy cover, average canopy.
def get_irrigation_data(plantingId):
    url = f"{base_url_v2}plantings/{plantingId}/irrigation-events/details." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/plantings/{plantingId}/irrigation-events/recommendation-summary.{ext}?eventDate={eventDate}&irrigationMethodId={irrigationMethodId}&eventId={eventId}&customDeficit={customDeficit}
# Get an irrigation recommendation depending on various inputs, including event date, and irrigation method.
def get_custom_irrigation_recommendation(plantingId, eventDate, irrigationMethodId, eventId=None, customDeficit=None):
    url = f"{base_url_v2}plantings/{plantingId}/irrigation-events/recommendation-summary." + "{ext}" + f"?eventDate={eventDate}&irrigationMethodId={irrigationMethodId}&eventId={eventId}&customDeficit={customDeficit}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/plantings/{plantingId}/wells.{ext}
# Returns a list of wells associated with a planting.
def get_planting_wells(plantingId):
    url = f"{base_url_v2}plantings/{plantingId}/wells." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/maturities.{ext}
# Returns a list of maturities, used primarily for Alfalfa.
def get_maturities():
    url = f"{base_url_v2}maturities." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/microsprinklers.{ext}
# Returns a list of micro sprinklers.
def get_microsprinklers():
    url = f"{base_url_v2}microsprinklers." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/plantings/{id}.{ext}
# Returns planting details.
def get_planting_details(planting_id):
    url = f"{base_url_v2}plantings/{planting_id}." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/plantings/{plantingId}/events.{ext}
# Returns events from a specific planting.
def get_planting_events(plantingId):
    url = f"{base_url_v2}plantings/{plantingId}/events." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/plantings/{plantingId}/rainfall.{ext}
# Returns rainfall data.
def get_planting_rainfall(plantingId):
    url = f"{base_url_v2}plantings/{plantingId}/rainfall." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/plantings/{plantingId}/totals/applied-water.json?startDate={startDate}&endDate={endDate}
# Given planting ID, start and end dates, return total applied water.
def get_total_applied_water(plantingId, startDate, endDate):
    url = f"{base_url_v2}plantings/{plantingId}/totals/applied-water.json?startDate={startDate}&endDate={endDate}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{ranchGuid}/plantings.{ext}?active={active}&commodityTypeId={commodityTypeId}
# Returns a list of plantings from a specific ranch. The list can be filtered to only return active plantings or plantings associated with a specific commodity type.
def get_ranch_plantings(ranchGuid, active=True, commodityTypeId=None):
    url = f"{base_url_v2}ranches/{ranchGuid}/plantings." + "{ext}" + f"?active={active}&commodityTypeId={commodityTypeId}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches.{ext}
# Returns a list of ranches that the user has access to.
def get_ranches():
    url = f"{base_url_v2}ranches." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{ranchGuid}.json
# Returns basic ranch information.
def get_ranch_details(ranch_guid):
    url = f"{base_url_v2}ranches/{ranch_guid}.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{ranchGuid}/permissions.{ext}
# Retrieves a user's ranch planting permissions.
def get_ranch_planting_permissions(ranchGuid):
    url = f"{base_url_v2}ranches/{ranchGuid}/permissions." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{ranchGuid}/users/{userId}/permissions.json
# Returns a user's ranch permissions.
def get_ranch_permissions(ranchGuid, userId):
    url = f"{base_url_v2}ranches/{ranchGuid}/users/{userId}/permissions.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/lots/{lotId}.json
# Returns planting area details.
def get_planting_area_details(lotId):
    url = f"{base_url_v2}lots/{lotId}.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{ranchGuid}/lots.json
# Returns a list of planting areas associated with a ranch.
def get_planting_areas(ranchGuid):
    url = f"{base_url_v2}ranches/{ranchGuid}/lots.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{id}/ranch-wells.{ext}
# Returns a list of wells associated with a ranch.
def get_wells(id):
    url = f"{base_url_v2}ranches/{id}/ranch-wells." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/wells/{wellId}.json
# Returns well details.
def get_well_details(wellId):
    url = f"{base_url_v2}wells/{wellId}.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/regions.{ext}
# Returns a list of regions in CropManage. Current regions are in California and Hawaii.
def get_regions():
    url = f"{base_url_v2}regions." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# GET v2/plantings/{plantingId}/soil-moisture-data.{ext}
# Returns soil moisture data for a planting.
def get_soil_moisture_data(plantingId):
    url = f"{base_url_v2}plantings/{plantingId}/soil-moisture-data." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/soil-types.{ext}
# Returns a list of all soil types in the database. This is a simple list of soil types. To retrieve soil types in more detail, call /soil-types/list.{ext}
def get_soil_types():
    url = f"{base_url_v2}soil-types." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# GET v2/soil-web.{ext}?lat={lat}&lng={lng}
# A simple call that retrieves soil web data, given coordinates. This call is intended to be used with single call web API which requires soil properties. Warning: This is restricted to registered 3rd party applications to prevent abuse.
def get_soil_data(lat, lng):
    url = f"{base_url_v2}soil-web." + "{ext}" + f"?lat={lat}&lng={lng}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/tissue-sample-events/{id}.{ext}
# Returns tissue sample event details.
def get_tissue_sample_event_details(id):
    url = f"{base_url_v2}tissue-sample-events/{id}." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/tissue-sample-locations.{ext}
# Returns a list of tissue sample locations.
def get_tissue_sample_locations():
    url = f"{base_url_v2}tissue-sample-locations." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/tissue-sample-nutrients.{ext}
# Returns a list of tissue sample nutrients.
def get_tissue_sample_nutrients():
    url = f"{base_url_v2}tissue-sample-nutrients." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/user-detail.{ext}
# Get current logged in user's information.
def get_user_details():
    url = f"{base_url_v2}user-detail." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{ranchGuid}/users.json
# Get users associated with a ranch.
def get_associated_users(ranchGuid):
    url = f"{base_url_v2}ranches/{ranchGuid}/users.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/weatherapis.{ext}
# This controller is used to access Weather service records, like CIMIS, and HoboLink.
def get_weather_service_records():
    url = f"{base_url_v2}weatherapis." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/ranches/{ranchGuid}/weather-stations.{ext}
# Returns weather stations associated with a ranch.
def get_weather_stations_by_ranch(ranch_guid):
    url = f"{base_url_v2}ranches/{ranch_guid}/weather-stations." + "{ext}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/weather-stations.{ext}?activeOnly={activeOnly}&ranchGuid={ranchGuid}&suppressZeroET={suppressZeroET}
# Returns all weather stations in the database.
def get_all_weather_stations(active_only=False, ranch_guid=None, suppress_zero_et=False):
    url = f"{base_url_v2}weather-stations.json?activeOnly={active_only}&ranchGuid={ranch_guid}&suppressZeroET={suppress_zero_et}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# (COULD NOT TEST)
# GET v2/weather-stations/{id}.{ext}?ranchGuid={ranchGuid}
# Get details for a specific weather station.
def get_weather_station_details(id, ranchGuid=None):
    url = f"{base_url_v2}weather-stations/{id}." + "{ext}" + f"?ranchGuid={ranchGuid}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code

# GET v2/weather-stations/{stationId}/missingRecords.json
# Get missing station records for a weather station.
def get_missing_station_records(stationId):
    url = f"{base_url_v2}weather-stations/{stationId}/missingRecords.json"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else response.status_code