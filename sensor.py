
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

SENSOR_TYPES = {
    "example_key": "Example Sensor"
}


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the Enphase-ChargeHQ sensors."""
    coordinator = hass.data["enphase_chargehq"][entry.entry_id]
    async_add_entities(
        EnphaseChargeHQSensor(coordinator, sensor) for sensor in SENSOR_TYPES
    )


class EnphaseChargeHQSensor(CoordinatorEntity, SensorEntity):
    """Representation of an Enphase-ChargeHQ sensor."""

    def __init__(self, coordinator, sensor):
        super().__init__(coordinator)
        self._sensor = sensor

    @property
    def name(self):
        return SENSOR_TYPES[self._sensor]

    @property
    def state(self):
        return self.coordinator.data.get(self._sensor)
