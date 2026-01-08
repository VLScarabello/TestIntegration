
import asyncio
from homeassistant.core import HomeAssistant

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_IP_ADDRESS,
    CONF_USERNAME,
    CONF_PASSWORD,
)
import homeassistant.helpers.entity_registry
from .const import DOMAIN

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Test component from YAML."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    hass.data.setdefault(DOMAIN, {})
    host = entry.data.get(CONF_IP_ADDRESS)
    username = entry.data.get(CONF_USERNAME)
    password = entry.data.get(CONF_PASSWORD)
    await hass.async_create_task(
            hass.config_entries.async_forward_entry_setups(
                entry,
                [
                    "switch"
                ],
            )
        )