from homeassistant.components.switch import SwitchEntity

from homeassistant.helpers.entity import DeviceInfo, Entity
from homeassistant.helpers.entity import EntityCategory
from homeassistant.core import HomeAssistant

from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import BRAND, DOMAIN

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    switches = [TestSwitchEntity()]
    async_add_entities(switches)

class TestSwitchEntity(SwitchEntity, Entity):
    def __init__(self):
        self._enabled = False 
        Entity.__init__(self)
        SwitchEntity.__init__(self)
        self._attr_state = "off"

    @property
    def name(self) -> str:
        return "Test Paolo"

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
        identifiers={(DOMAIN, "TEST_SWITCH")},
        connections={("mac", "FFFF:FFFF:FFFF:FFFF")},
        name="Paolo",
        manufacturer=BRAND,
        model="Paolo Switch",
        sw_version="1.0.0b",
        hw_version="1.0v1b",
    )

    @property
    def unique_id(self) -> str:
        return "TEST-PAOLO-MAO"

    @property
    def model(self):
        return "Paolo Switch"

    @property
    def brand(self):
        return BRAND

    async def async_added_to_hass(self) -> None:
        self._enabled = True

    async def async_will_remove_from_hass(self) -> None:
        self._enabled = False
    
    @property
    def entity_category(self):
        return EntityCategory.CONFIG

    @property
    def state(self):
        return self._attr_state
    
    async def async_turn_on(self) -> None:
        self._attr_state = "on"

    async def async_turn_off(self) -> None:
        self._attr_state = "off"