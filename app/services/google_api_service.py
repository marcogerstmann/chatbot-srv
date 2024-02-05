import requests

from app.backend.settings import settings
from app.constants import MIN_SOLAR_API_IMAGE_QUALITY
from app.schemas.google_geocoding_result_schema import GoogleGeocodingResultsSchema, GoogleGeocodingLocationSchema
from app.schemas.google_solar_building_insights_response_schema import GoogleSolarBuildingInsightResponseSchema


# TODO: Add error handling for these 3rd party API calls (and error handling in general)

def get_coordinates(address: str) -> GoogleGeocodingLocationSchema:
    response = requests.get(
        "https://maps.googleapis.com/maps/api/geocode/json"
        f"?address={address}"
        f"&key={settings.google_cloud_api_key}"
    )
    location = GoogleGeocodingResultsSchema.model_validate(response.json()).results[0].geometry.location
    print(f"Coordinates for {address}: lat {location.lat} lng {location.lng}")  # TODO: Use logger instead
    return location


def get_solar_building_insights(coordinates: GoogleGeocodingLocationSchema) -> GoogleSolarBuildingInsightResponseSchema:
    response = requests.get(
        "https://solar.googleapis.com/v1/buildingInsights:findClosest"
        f"?location.latitude={coordinates.lat}"
        f"&location.longitude={coordinates.lng}"
        f"&requiredQuality={MIN_SOLAR_API_IMAGE_QUALITY}"
        f"&key={settings.google_cloud_api_key}"
    )
    return GoogleSolarBuildingInsightResponseSchema.model_validate(response.json())
