

from __future__ import annotations

import asyncio

from homeassistant.helpers.discovery import load_platform
from homeassistant.const import Platform

DOMAIN = "test_integration"
PLATFORMS = [Platform.SWITCH]

async def async_setup_entry(hass, entry):
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True