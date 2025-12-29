

from __future__ import annotations

from homeassistant.helpers.discovery import load_platform

DOMAIN = "test_integration"

def setup(hass, config):
    hass.states.async_set("test_integration.state", False)

    load_platform(hass, 'switch', DOMAIN, {}, config)
    
    return True