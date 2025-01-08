from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

SENSOR_TYPES = {
    "production_kw": "Production (kW)",
    "consumption_kw": "Consumption (kW)",
    "net_import_kw": "Net Import (kW)",
    "imported_kwh": "Imported (kWh)",
    "exported_kwh": "Exported (kWh)"
}


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the ChargeHQ sensors."""
    coordinator = hass.data["chargehq"][entry.entry_id]
    async_add_entities(
        ChargeHQSensor(coordinator, sensor) for sensor in SENSOR_TYPES
    )


class ChargeHQSensor(CoordinatorEntity, SensorEntity):
    """Representation of a ChargeHQ sensor."""

    def __init__(self, coordinator, sensor):
        super().__init__(coordinator)
        self._sensor = sensor

    @property
    def name(self):
        return SENSOR_TYPES[self._sensor]

    @property
    def state(self):
        return self.coordinator.data.get(self._sensor)
