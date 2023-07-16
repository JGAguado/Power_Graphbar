[![hacs][hacs-shield]][hacs]
[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE)

[![Project Maintenance][maintenance-shield]][maintenance]
[![BuyMeCoffee][buymecoffee-shield]][buymecoffee]

# Power Graphbar

This integration generates an entity whose attributes are the graphic bar coordinates (X,Y) based on hourly/dayly power consumption.

This can be used later on to pass an ESPHome device with an e-Ink display, the array of monthly days with the coordinates in order to plot them correctly.


# Configuration

The integration requires the following parameters as arguments:

Parameter | Value(example)
-- | --
hourly | [120, 25, 158, 38, 24]
daily | [120, 81, 158, 30, 7]
consumption | `1.54`
history | [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]


## Example
On the configuration.yml :

```yaml
sensor:
  - platform: power_graphbar
    name: Graphic_power
    hourly: [120, 25, 158, 38, 24]
    daily: [120, 81, 158, 30, 7]
    consumption: sensor.total_daily_power
    history: sensor.graphic_power.history
```
Output generated dictionary :

```
'hours': {0: [122, 63.0, 4, 0.0], 1: [128, 63.0, 4, 0.0], 2: [135, 63.0, 4, 0.0], 3: [141, 63.0, 4, 0.0], 4: [148, 63.0, 4, 0.0], 5: [154, 63.0, 4, 0.0], 6: [161, 63.0, 4, 0.0], 7: [168, 63.0, 4, 0.0], 8: [174, 63.0, 4, 0.0], 9: [181, 63.0, 4, 0.0], 10: [187, 63.0, 4, 0.0], 11: [194, 63.0, 4, 0.0], 12: [201, 63.0, 4, 0.0], 13: [207, 63.0, 4, 0.0], 14: [214, 63.0, 4, 0.0], 15: [220, 63.0, 4, 0.0], 16: [227, 63.0, 4, 0.0], 17: [233, 63.0, 4, 0.0], 18: [240, 25.0, 4, 38.0], 19: [247, 63.0, 4, 0.0], 20: [253, 63.0, 4, 0.0], 21: [260, 63.0, 4, 0.0], 22: [266, 63.0, 4, 0.0], 23: [273, 63.0, 4, 0.0]}

'days':{0: [122, 111.0, 20, 0.0], 1: [144, 111.0, 20, 0.0], 2: [167, 111.0, 20, 0.0], 3: [189, 111.0, 20, 0.0], 4: [212, 111.0, 20, 0.0], 5: [234, 111.0, 20, 0.0], 6: [257, 81.0, 20, 30.0]}

'history': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.38, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1.38]]

```





[hacs-shield]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[hacs]: https://github.com/custom-components/hacs

[releases-shield]: https://img.shields.io/github/release/JGAguado/Power_Graphbar.svg?style=for-the-badge
[releases]: https://github.com/JGAguado/Power_Graphbar/releases

[license-shield]: https://img.shields.io/github/license/JGAguado/Power_Graphbar.svg?style=for-the-badge

[maintenance-shield]: https://img.shields.io/badge/maintainer-J.%20G.%20Aguado-blue.svg?style=for-the-badge
[maintenance]: https://github.com/JGAguado

[buymecoffee-shield]: https://img.shields.io/badge/buy%20me%20a%20coffee-support-yellow.svg?style=for-the-badge
[buymecoffee]: https://www.buymeacoffee.com/J.G.Aguado

