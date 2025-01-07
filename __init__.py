
from datetime import timedelta
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN, FETCH_INTERVAL

_LOGGER = logging.getLogger(__name__)
PLATFORMS = ["sensor"]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Enphase-ChargeHQ from a config entry."""
    coordinator = EnphaseChargeHQDataUpdateCoordinator(hass, entry.data)
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


class EnphaseChargeHQDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Enphase-ChargeHQ data."""

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
            # Logic to fetch and process data
            return {"example_key": "example_value"}
        except Exception as err:
            raise UpdateFailed(f"Error updating data: {err}")
