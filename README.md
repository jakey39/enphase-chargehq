# Enphase-ChargeHQ Home Assistant Integration

This is a custom integration for Home Assistant to integrate ChargeHQ with Enphase Envoy data.

## Features
- Monitor production, consumption, and net import/export of energy.

## Installation

### Option 1: Add via "My Integration"
Click the button below to add the integration directly to Home Assistant:

[![Open your Home Assistant instance and show the Enphase-ChargeHQ dashboard.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start?domain=enphase_chargehq)

### Option 2: Manual Installation
1. Copy the `custom_components/enphase_chargehq` folder into your Home Assistant's `custom_components` directory.
2. Restart Home Assistant.
3. Add the Enphase-ChargeHQ integration via the Home Assistant UI.

## Lovelace Dashboard
Use the following configuration to display data:
```yaml
title: Enphase-ChargeHQ Dashboard
views:
  - title: Solar Overview
    cards:
      - type: entities
        entities:
          - entity: sensor.example_key
```
