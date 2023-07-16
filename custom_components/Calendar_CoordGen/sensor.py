"""
Graphicbar Power Coordinates Generator for Home Assistant
------------------------------------------------------------
%   Description: Script for generating graphic bar coordinates (X,Y) based on hourly/dayly power consumption
%   Author: J.G.Aguado
%   Date of creation: 16/07/2023
------------------------------------------------------------
"""

import logging

import datetime
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_API_KEY, CONF_NAME
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity
import voluptuous as vol

_LOGGER = logging.getLogger(__name__)

DOMAIN = "sensor"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required("hourly"): vol.All(cv.ensure_list, [cv.string]),
        vol.Required("daily"): vol.All(cv.ensure_list, [cv.string]),
        vol.Required("consumption"): cv.string,
        vol.Required("history"): vol.All(cv.ensure_list, [cv.string]),
        vol.Required(CONF_NAME): cv.string,
    }
)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the fuel tracker sensor."""

    _LOGGER.info("init sensor")
    name = config.get(CONF_NAME)
    hourly = config.get("hourly")
    daily = config.get("daily")
    consumption = config.get("consumption")
    history = config.get("history")

    fn = ConsumptionData(name, hourly, daily, consumption, history)

    if not fn:
        _LOGGER.error("Unable to create the sensor")
        return

    add_entities([ConsumptionSensor(hass, fn)], True)


class ConsumptionSensor(Entity):
    def __init__(self, hass, fn):
        self._hass = hass
        self.data = fn

    @property
    def name(self):
        """Return the name of the sensor."""
        return "{}".format(self.data.name)

    @property
    def state(self):
        """Return the state of the device."""
        return True

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return self.data.attr
        
    @property
    def icon(self):
        return "mdi:counter"
    
    def update(self):
        self.data.get_consumption()


class ConsumptionData:
    def __init__(self, name, hourly, daily, consumption, history=None):
        self.name = name
        self.attr = {}
        self.get_consumption(hourly, daily, consumption, history)

    def get_consumption(self, hourly, daily, consumption, history, separator=4):
        minute = datetime.datetime.now().minute
        hour = datetime.datetime.now().hour
        day = datetime.date.today().weekday()
        coordinates = {}

        if (history is None) or (day == 6 and hour == 0 and minute == 0):
            history = [[0] * 24, [0] * 7]

        mapping = ['hours', 'days']
        for index, timeframe in enumerate([hourly, daily]):
            x, y, w, h, bars = timeframe
            coordinates[index] = {}
            v_max = 0
            if index == 0:
                history[index][hour] = consumption
            else:
                history[index][day] = consumption

            for bar in range(bars):
                if history[index][bar] > v_max:
                    v_max = history[index][bar]

            for bar in range(bars):
                v = h * (history[index][bar] / v_max)
                coordinates[index][bar] = [int(x + bar * (w/bars) + separator / 2), y + h - v, int(w / bars - separator / 2), v]

            self.attr[mapping[index]] = coordinates[index]
        self.attr['history'] = history
