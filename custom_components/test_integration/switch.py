from homeassistant.components.switch import SwitchEntity

def setup_platform(
    hass,
    config,
    add_entities,
    discovery_info
):
    """Set up the test switch"""

    # Add devices
    add_entities([MySwitch()])

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
