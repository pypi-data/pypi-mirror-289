to_wgs = [
    {
        "name": "Google Maps",
        "url": "\thttps://maps.google.com/maps?q=loc:{lat}+{lon}&t=k",
    },
    {
        "name": "Google Earth",
        "url": "\thttps://earth.google.com/web/@{lat},{lon},20000.44000000d",
    },
    {
        "name": "EO Browser",
        "url": "\thttps://apps.sentinel-hub.com/eo-browser/?zoom=18&lat={lat}&lng={lon}",
    },
    {
        "name": "Yandex Maps",
        "url": "\thttps://yandex.com/maps/?ll={lon}%2C{lat}&pt={lon},{lat}&z=18&l=sat",
    },
    {
        "name": "Bing Maps",
        "url": "\thttps://bing.com/maps/default.aspx?cp={lat}~{lon}&style=h&lvl=19&sp=point.{lat}_{lon}",
    },
    {
        "name": "PeakVisor",
        "url": "\thttps://peakvisor.com/panorama.html?lat={lat}&lng={lon}",
    },
]
to_gcj = [
    {
        "name": "Google Maps (switch to plan/roadmap view if needed)",
        "url": "\thttps://maps.google.com/maps?q=loc:{lat}+{lon}&t=m",
    },
    {
        "name": "Bing Maps",
        "url": "\thttps://bing.com/maps/default.aspx?cp={lat}~{lon}&style=r&lvl=19&sp=point.{lat}_{lon}",
    },
]
wgs_to_bd = [
    {
        "name": "Baidu Map",
        "url": "\thttp://api.map.baidu.com/marker?location={lat},{lon}&output=html",
    },
]
wgs_to_gcj = [
    {
        "name": "Amap Map",
        "url": "\thttp://uri.amap.com/marker?position={lon},{lat}",
    },
    {
        "name": "QQ Map",
        "url": "\thttps://map.qq.com/?type=marker&isopeninfowin=0&markertype=1&pointx={lon}&pointy={lat}&name=X",
    }
]
