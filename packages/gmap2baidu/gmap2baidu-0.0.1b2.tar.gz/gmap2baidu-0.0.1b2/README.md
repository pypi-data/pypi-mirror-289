# gmap2baidu

<p align="center">
  <img src="https://raw.githubusercontent.com/balestek/gmap2baidu/master/media/gmap2baidu-logo.png">
</p>

## Description

_gmap2baidu_ is a wrapper for prcoords library to convert Google / Bing Maps / Sat imagery coordinates in decimal degrees (WGS-84 or GCJ-02) to Baidu Map (BD-09) or other chinese maps.

## Installation

### Using pipx

```bash
pipx install gmap2baidu
```

To run without installing:

```bash
pipx run gmap2baidu [options] latitude longitude # see Usage
```

## Usage

Latitude and longitude are in decimal degrees, E.g. 31.241851345365674 121.49525353462117.

### From WGS-84 to Chinese maps

option `-wgs`

From:
- Google Maps satellite view
- Bing Maps satellite view
- Yandex Maps satellite view and roadmap view
- Satellite imagery,...

`gmap2baidu -wgs latitude longitude`

```bash
gmap2baidu -wgs 31.241860527043016 121.49525795996406
```

### From GCJ-02 to chinese maps

option `-gcj`

From:
- Google Maps roadmap view
- Bing Maps roadmap view
- Chinese maps satellite and roadmap view (to get Baidu BD-09 coordinates)

`gmap2baidu -gcj latitude longitude`

```bash
gmap2baidu gmap2baidu -gcj 31.239773035270655 121.49961209129178
```

### From Baidu BD-09 to non chinese maps

option `-r -bd`

- From Baidu Maps satellite view and roadmap view

`gmap2baidu -r -bd latitude longitude`

```bash
gmap2baidu -r -bd 31.245501027853667 121.50631784536566
```
### From GCJ-02 to non chinese maps

option `-r -gcj`

From:
- Amap.com
- map.qq.com
- other chinese GCJ-02 maps

`gmap2baidu -r -gcj latitude longitude`

```bash
gmap2baidu -r -gcj 31.239760876521242 121.49961227600687
```

### Fetch basic location information

option `-i`

Fetch basic location information from an Amap undocumented endpoint, translated to english with Google Translate: 
`Country, Country code, Province, City, District, Administration code, Phone code.`

```bash
gmap2baidu -wgs -i 31.241860527043016 121.49525795996406
```

## Credits

- prcoords
- colorama
- easygoogletranslate

## License

GPLv3
