<h1 style="text-align: center;">AIFS Fellowship: DG + CropManage Chatbot</h1>

- <b>get_requests.py</b>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> File containing methods for all of the GET requests available on the CropManage API.

- <b>post_requests.py</b>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> File containing methods for all of the POST requests available on the CropManage API.

- <b>put_requests.py</b>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> File containing methods for all of the PUT requests available on the CropManage API.

- <b>delete_requests.py</b>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> File containing methods for all of the DELETE requests available on the CropManage API.

- <b>example.py</b>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> Sample program to test communication with the CropManage API.

- <b>README.md</b>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> Markdown file containing descriptions of all files included.</p>


<h2 style="text-align: center;">ChatBot Functionality</h2>
<b>-> A list of all the CropManage API endpoints that the chatbot is currently able to access. Tentative to change.</b><br><br>

**CropManage API Documentation: [https://api.cropmanage.ucanr.edu/help](https://api.cropmanage.ucanr.edu/help)**

**The chatbot can…**



* Return a list of commodity types in CropManage. *(GET v2/commodity-types.json)*
* Return a list of crop stages associated with a commodity type. *(GET v2/crop-stages.json?commodityTypeId={commodityTypeId})*
* Return a list of all crop types in the system. *(GET v2/crop-types.{ext}?includePrevious={includePrevious}&commodityTypeId={commodityTypeId})*
* Get crop type data, based on ID. *(GET v2/crop-types/{cropTypeId}.{ext})*
* Return a list of crop types associated with a ranch. Normally, a ranch is only associated with a handful of commodity types and a select number of crop types. *(GET v2/ranches/{ranchGuid}/commodity-types/{commodityTypeId}/crop-types.{ext}?shouldFilterUnassociated={shouldFilterUnassociated})*
* Return a list of ET data associated with a planting. *(GET v2/plantings/{plantingId}/et-weather-events.json)*
* Return a fertilization event. *(GET v2/fertilization-events/{id}.{ext})*
* Return a list of wells associated with a fertilization event. *(GET v2/fertilization-events/{eventId}/wells.{ext})*
* Return a well associated with a fertilization event. *(GET v2/fertilization-event-wells/{Id}.{ext})*
* Return a list of fertilizers associated with a ranch. *(GET v2/ranches/{ranchGuid}/fertilizers.{ext})*
* Return a list of fertilizers that are not associated with the ranch but are available for use. *(GET v2/ranches/{ranchGuid}/fertilizers/available.{ext})*
* Return an irrigation event. *(GET v2/irrigation-events/{id}.{ext})*
* Return CropManage irrigation interval recommendation for a specific irrigation event. *(GET v2/irrigation-events/{id}/recommendations-interval-summary.{ext})*
* Returns detailed irrigation data for a planting, including reference ET, canopy cover, average canopy. *(GET v2/plantings/{plantingId}/irrigation-events/details.{ext})*
* Get an irrigation recommendation depending on various inputs, including event date, and irrigation method. *(GET v2/plantings/{plantingId}/irrigation-events/recommendation-summary.{ext}?eventDate={eventDate}&irrigationMethodId={irrigationMethodId}&eventId={eventId}&customDeficit={customDeficit})*
* Return a list of wells associated with a planting. *(GET v2/plantings/{plantingId}/wells.{ext})*
* Return a list of maturities, used primarily for Alfalfa. *(GET v2/maturities.{ext})*
* Return a list of micro sprinklers. *(GET v2/microsprinklers.{ext})*
* Return planting details. *(GET v2/plantings/{id}.{ext})*
* Return events from a specific planting. *(GET v2/plantings/{plantingId}/events.{ext})*
* Return rainfall data. *(GET v2/plantings/{plantingId}/rainfall.{ext})*
* Given planting ID, start and end dates, return total applied water. *(GET v2/plantings/{plantingId}/totals/applied-water.json?startDate={startDate}&endDate={endDate})*
* Return a list of plantings from a specific ranch. *(GET v2/ranches/{ranchGuid}/plantings.{ext}?active={active}&commodityTypeId={commodityTypeId})*
* Return a list of ranches that the user has access to. *(GET v2/ranches.{ext})*
* Return basic ranch information. *(GET v2/ranches/{ranchGuid}.json)*
* Retrieve a user’s ranch planting permissions. *(GET v2/ranches/{ranchGuid}/permissions.{ext})*
* Return a user’s ranch permissions. *(GET v2/ranches/{ranchGuid}/users/{userId}/permissions.json)*
* Return planting area details. *(GET v2/lots/{lotId}.json)*
* Return a list of planting areas associated with a ranch. *(GET v2/ranches/{ranchGuid}/lots.json)*
* Return a list of wells associated with a ranch. *(GET v2/ranches/{id}/ranch-wells.{ext})*
* Return well details. *(GET v2/wells/{wellId}.json)*
* Return a list of regions in CropManage. *(GET v2/regions.{ext})*
* Return a list of all soil types in the database. *(GET v2/soil-types.{ext})*
* Return tissue sample event details. *(GET v2/tissue-sample-events/{id}.{ext})*
* Return a list of tissue sample locations. *(GET v2/tissue-sample-locations.{ext})*
* Return a list of tissue sample nutrients. *(GET v2/tissue-sample-nutrients.{ext})*
* Get current logged in user’s information. *(GET v2/user-detail.{ext})*
* Get users associated with a ranch. *(GET v2/ranches/{ranchGuid}/users.json)*
* Access weather service records, like CIMIS, and HoboLink. *(GET v2/weatherapis.{ext})*
* Return weather stations associated with a ranch. *(GET v2/ranches/{ranchGuid}/weather-stations.{ext})*
* Return all weather stations in the database. *(GET v2/weather-stations.{ext}?activeOnly={activeOnly}&ranchGuid={ranchGuid}&suppressZeroET={suppressZeroET})*
* Get missing station records. *(GET v2/weather-stations/{stationId}/missingRecords.json)*
* Save a commodity type ranch association. *(POST v2/ranches/{ranchGuid}/commodity-types.{ext})*
* Get a fertilizer recommendation. *(POST v2/fertilization-recommendation.{ext})*
* Add a fertilizer to a ranch. *(POST v2/ranches/{ranchGuid}/fertilizers/{fertilizerId}.{ext})*
* Get an irrigation recommendation. *(POST v2/irrigation-recommendation.{ext})*
* Access public ET calculator. *(POST v2/season-et.{ext})*
* Create a new ranch. *(POST v3/ranches.{ext})*


**The chatbot cannot…**



* Return cut event data. *(GET v2/cut-events/{id}.{ext})*
* Get CropManage recommendation for a fertilizer event. *(GET v2/fertilization-events/{id}/recommendation.{ext}?soilSampleEventDate={soilSampleEventDate}&daysToNextFertilization={daysToNextFertilization}&fertilizationsPerMonth={fertilizationsPerMonth}&eventDate={eventDate}&nInWater={nInWater})*
* Check whether an irrigation event already exists on a specific date, to prevent multiple irrigation events from being created on the same date. *(GET v2/plantings/{plantingId}/irrigation-events/count-events-on-date.{ext}?targetDate={targetDate})*
* Return soil moisture data for a planting. *(GET v2/plantings/{plantingId}/soil-moisture-data.{ext})*
* Retrieve soil web data, given coordinates. *(GET v2/soil-web.{ext}?lat={lat}&lng={lng})*
* Get details for a specific weather station. *(GET v2/weather-stations/{id}.{ext}?ranchGuid={ranchGuid})*
* Create or update a cut event. *(POST v2/cut-events.{ext})*
* Save an ET weather event. *(POST v2/et-weather-events.{ext})*
* Create a new fertilization event. *(POST v2/plantings/{plantingId}/fertilization-events.{ext})*
* Get multiple irrigation recommendations. *(POST v2/irrigation-recommendations.{ext})*
* Create an irrigation event. *(POST v3/plantings/{plantingId}/irrigation-events.{ext})*
* Create a new planting. *(POST v3/ranches/{ranchGuid}/plantings.json)*
* Create a new planting area. *(POST v3/ranches/{ranchGuid}/lots.json)*
* Add a well to a ranch. *(POST v2/ranches/{ranchGuid}/wells.json)*
* Create a new soil sample event. *(POST v2/plantings/{plantingId}/soil-sample-events.{ext})*
* Create tissue sample event. *(POST v3/plantings/{plantingId}/tissue-sample-events.{ext})*
* Add a user to a ranch. *(POST v2/ranches/{ranchGuid}/users/{userId}.json)*
* Add weather stations to a ranch. *(POST v2/ranches/{ranchGuid}/weather-stations.{ext})*
* Update a fertilization event. *(PUT v2/fertilization-events/{id}.{ext})*
* Update an irrigation event. *(PUT v3/irrigation-events/{id}.{ext})*
* Update a planting. *(PUT v3/plantings/{plantingId}.json)*
* Update ranch information. *(PUT v3/ranches/{ranchGuid}.json)*
* Update a planting area. *(PUT v3/lots/{id}.json)*
* Update a well. *(PUT v2/ranches/{ranchGuid}/wells/{wellId}.json)*
* Update a soil sample event. *(PUT v2/soil-sample-events/{id}.{ext})*
* Update tissue sample event. *(PUT v3/tissue-sample-events/{eventId}.{ext})*
* Delete a cut event. *(DELETE v2/cut-events/{id}.{ext})*
* Delete a fertilization event. *(DELETE v2/fertilization-events/{id}.{ext})*
* Delete a fertilizer from a ranch. *(DELETE v2/ranches/{ranchGuid}/fertilizers/{id}.{ext})*
* Delete an irrigation event. *(DELETE v2/irrigation-events/{id}.{ext})*
* Delete a planting. *(DELETE v2/plantings/{plantingId}.{ext})*
* Delete a ranch. *(DELETE v2/ranches/{ranchGuid}.json)*
* Delete a planting area from a ranch. *(DELETE v2/lots/{lotId}.json)*
* Delete a well from a ranch. *(DELETE v2/ranches/{ranchGuid}/wells/{wellId}.json)*
* Delete a soil sample event. *(DELETE v2/soil-sample-events/{id}.{ext})*
* Delete tissue sample event. *(DELETE v2/tissue-sample-events/{id}.{ext})*
* Remove user from a ranch. *(DELETE v2/ranches/{ranchGuid}/users/{userIdTarget}.json)*
* Delete weather station from a ranch. *(DELETE v2/ranches/{ranchGuid}/weather-stations/{stationId}.{ext})*
