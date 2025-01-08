from datetime import timedelta
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN, FETCH_INTERVAL, CHARGEHQ_API_KEY, ENVOY_ACCESS_TOKEN, ENVOY_LOCAL_IP, VERIFY_SSL

_LOGGER = logging.getLogger(__name__)
PLATFORMS = ["sensor"]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up ChargeHQ from a config entry."""
    coordinator = ChargeHQDataUpdateCoordinator(hass, entry.data)
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator
    await coordinator.async_config_entry_first_refresh()
    hass.config_entries.async_setup_platforms(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok


class ChargeHQDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching ChargeHQ data."""

    def __init__(self, hass: HomeAssistant, config: dict):
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=config.get(FETCH_INTERVAL, 60)),
        )
        self.config = config

    async def _async_update_data(self):
        """Fetch data from Envoy and calculate values."""
        try:
            envoy_data = await fetch_envoy_data(self.config)
            return calculate_values(envoy_data)
        except Exception as err:
            raise UpdateFailed(f"Error updating data: {err}")
