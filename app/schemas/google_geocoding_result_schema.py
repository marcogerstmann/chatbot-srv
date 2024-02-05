from app.schemas.base_schema import BaseSchema


class GoogleGeocodingLocationSchema(BaseSchema):
    lat: float
    lng: float


class GoogleGeocodingGeometrySchema(BaseSchema):
    location: GoogleGeocodingLocationSchema


class GoogleGeocodingResultSchema(BaseSchema):
    geometry: GoogleGeocodingGeometrySchema


class GoogleGeocodingResultsSchema(BaseSchema):
    results: list[GoogleGeocodingResultSchema]
