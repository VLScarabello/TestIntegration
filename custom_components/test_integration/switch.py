from homeassistant.components.switch import SwitchEntity

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: HubConfigEntry,
    async_add_entities: AddEntitiesCallback,
):
    """Set up the test switch"""

    # Add devices
    async_add_entities([MySwitch()])

class MySwitch(SwitchEntity):

    def __init__(self):
        self._state = False

    async def async_turn_on(self, **kwargs):
        """Turn the entity on."""
        self._state = True

    async def async_turn_off(self, **kwargs):
        """Turn the entity on."""
        self._state = False
    
    @property
    def is_on(self):
        return self._state
