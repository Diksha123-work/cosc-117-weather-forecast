from backend import calc_aqi_level
from config import AQI_INTERVALS

def test_so2_level_calculation():
    assert calc_aqi_level("77", AQI_INTERVALS["so2"]) == 2

def test_co_level_calculation():
    assert calc_aqi_level("684.85", AQI_INTERVALS["co"]) == 1  