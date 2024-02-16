import math

from app.constants import AVG_COST_PER_KWH, DC_TO_AC_RATE
from app.schemas.google_solar_building_insights_response_schema import (
    GoogleSolarPanelConfig,
)
from app.schemas.solar_potential_response_schema import SolarPotentialResponseSchema
from app.services.google_api_service import get_coordinates, get_solar_building_insights


def calculate_solar_potential(
    address: str, max_solar_panels_percentage: float
) -> SolarPotentialResponseSchema:
    coordinates = get_coordinates(address)
    building_insights = get_solar_building_insights(coordinates)

    solar_panel_configs = building_insights.solar_potential.solar_panel_configs
    solar_panel_config = find_solar_panel_config_closest_to_max_panels(
        solar_panel_configs,
        building_insights.solar_potential.max_array_panels_count,
        max_solar_panels_percentage,
    )

    yearly_production_ac_kwh = solar_panel_config.yearly_energy_dc_kwh * DC_TO_AC_RATE
    yearly_production_ac_euro = yearly_production_ac_kwh * AVG_COST_PER_KWH

    return SolarPotentialResponseSchema(
        max_solar_panels_percentage=max_solar_panels_percentage,
        panels_count=solar_panel_config.panels_count,
        yearly_production_kwh=yearly_production_ac_kwh,
        yearly_production_euro=yearly_production_ac_euro,
    )


def enrich_solar_panel_configs(solar_panel_configs):
    for solar_panel_config in solar_panel_configs:
        solar_panel_config.yearly_energy_ac_kwh = (
            solar_panel_config.yearly_energy_dc_kwh * DC_TO_AC_RATE
        )
        solar_panel_config.yearly_energy_ac_euro = (
            solar_panel_config.yearly_energy_ac_kwh * AVG_COST_PER_KWH
        )


def find_solar_panel_config_closest_to_max_panels(
    solar_panel_configs: list[GoogleSolarPanelConfig],
    max_panels_count: int,
    max_solar_panels_percentage: float,
) -> GoogleSolarPanelConfig:
    target_panels_count = math.ceil(
        max_panels_count * (max_solar_panels_percentage / 100)
    )
    return next(
        filter(
            lambda solar_panel_config: solar_panel_config.panels_count
            == target_panels_count,
            solar_panel_configs,
        )
    )
