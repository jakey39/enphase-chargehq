
from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN


class EnphaseChargeHQConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Enphase-ChargeHQ."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Enphase-ChargeHQ", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("chargehq_api_key"): str,
                vol.Required("envoy_access_token"): str,
                vol.Required("envoy_local_ip"): str,
                vol.Optional("poll_interval", default=60): int,
            })
        )
