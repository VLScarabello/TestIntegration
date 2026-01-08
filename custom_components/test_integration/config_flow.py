import voluptuous as vol
from homeassistant.config_entries import HANDLERS, ConfigFlow
from homeassistant.const import (
    CONF_IP_ADDRESS,
    CONF_USERNAME,
    CONF_PASSWORD
)

from .const import (
    DOMAIN,
)


@HANDLERS.register(DOMAIN)
class FlowHandler(ConfigFlow):
    """Handle a config flow."""

    def __init__(self):
        ConfigFlow.__init__(self)

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        if user_input is not None:
            return self.async_create_entry(title="Test Switch", data=user_input)
        return await self.async_step_test()

    async def async_step_test(self, user_input=None):
        """Perform reauth upon an API authentication error."""
        
        return self.async_show_form(
            step_id="test",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_USERNAME, description={"suggested_value": "Paolo"}
                    ): str,
                    vol.Required(
                        CONF_PASSWORD, description={"suggested_value": "Paolo"}
                    ): str,
                    vol.Required(
                        CONF_IP_ADDRESS, description={"suggested_value": "192.168.1.15"}
                    ): str,
                }
            ),
            errors={},
            last_step=True,
        )