import argparse
import collections
import requests
import prcoords
from colorama import Fore, Style

import gmap2baidu.urls as urls
from easygoogletranslate import EasyGoogleTranslate


intro = f"""{Style.BRIGHT}                                               
  {Fore.BLUE}┌─┐┌┬┐┌─┐┌─┐ {Fore.YELLOW}┏┓{Fore.RED} ┌┐ ┌─┐┬┌┬┐┬ ┬
  {Fore.BLUE}│ ┬│││├─┤├─┘ {Fore.YELLOW}┏┛{Fore.RED} ├┴┐├─┤│ │││ │
  {Fore.BLUE}└─┘┴ ┴┴ ┴┴   {Fore.YELLOW}┗━{Fore.RED} └─┘┴ ┴┴─┴┘└─┘{Style.RESET_ALL}
  {Style.DIM}62 79 62 61 6c 65 73 74 65 6b{Style.RESET_ALL}

{Fore.WHITE}{Style.BRIGHT}Wrapper for prcoords library to convert Google / Bing Maps / Sat imagery coordinates in decimal degrees (WGS-84 or GCJ-02) to Baidu Map (BD-09) or other chinese maps.{Style.RESET_ALL}

{Fore.WHITE}{Style.BRIGHT}Usage:{Style.RESET_ALL}       {Fore.LIGHTCYAN_EX}gmap2baidu [-r] [-i] (-wgs | -gcj | -bd) latitude longitude{Fore.RESET}
             gmap2baidu -wgs latitude longitude     # Convert from WGS-84
             gmap2baidu -gcj latitude longitude     # Convert from GCJ-02
             gmap2baidu -r -bd latitude longitude   # Convert from BD-09
             gmap2baidu -r -gcj latitude longitude  # Convert from GCJ-02

{Fore.WHITE}{Style.BRIGHT}latitude:    {Style.RESET_ALL}{Fore.LIGHTCYAN_EX}float, latitude of the location in decimal degrees (DD)
{Fore.WHITE}{Style.BRIGHT}longitude:   {Style.RESET_ALL}{Fore.LIGHTCYAN_EX}float, longitude of the location in decimal degrees (DD){Fore.RESET}
{Fore.WHITE}{Style.BRIGHT}-r:          {Style.RESET_ALL}{Fore.LIGHTCYAN_EX}optional, convert from chinese systems{Fore.RESET}, see below
{Fore.WHITE}{Style.BRIGHT}-i:          {Style.RESET_ALL}{Fore.LIGHTCYAN_EX}optional, fetch and translate online basic information about the location{Fore.RESET}

{Fore.WHITE}{Style.BRIGHT}Options:{Style.RESET_ALL}{Fore.RESET}
{Fore.WHITE}{Style.BRIGHT}-wgs:        {Style.RESET_ALL}{Fore.LIGHTCYAN_EX}coordinates source from Google Maps satellite view, Bing Maps satellite view, Yandex roadmap or satellite view, satellite imagery
{Fore.WHITE}{Style.BRIGHT}-gcj:        {Style.RESET_ALL}{Fore.LIGHTCYAN_EX}coordinates source from Google Maps roadmap view, Bing Maps roadmap view
{Fore.WHITE}{Style.BRIGHT}-r -bd:      {Style.RESET_ALL}{Fore.LIGHTCYAN_EX}coordinates source from Baidu Map
{Fore.WHITE}{Style.BRIGHT}-r -gcj:     {Style.RESET_ALL}{Fore.LIGHTCYAN_EX}coordinates source from other chinese maps (Amap, QQ,...){Fore.RESET}

{Fore.WHITE}{Style.BRIGHT}Examples:   {Style.RESET_ALL} gmap2baidu -wgs 31.241860527043016 121.49525795996406
             gmap2baidu -gcj 31.239773035270655 121.49961209129178
             gmap2baidu -r -bd 31.245501027853667 121.50631784536566
             gmap2baidu -r -gcj 31.239760876521242 121.49961227600687
"""


def translate(data: dict) -> list:
    translator = EasyGoogleTranslate()
    details = []
    translated = None
    trans_ok = None
    keys = [
        "Country",
        "Country code",
        "Province",
        "City",
        "District",
        "Admin. code",
        "Phone code",
    ]
    infos = [
        data["country"],
        data["countrycode"],
        data["province"],
        data["city"],
        data["district"],
        data["adcode"],
        data["tel"],
    ]
    try:
        translated = translator.translate(f"{infos}", source_language="zh-CN", target_language='en')
        trans_ok = True
    except Exception as e:
        print(f"Can't translate : {e}")
        print("Information returned in chinese only")

    trans = eval(translated)

    for key, info, tran in zip(keys, infos, trans):
        if trans_ok is True:
            if key in ["Country code", "Admin. code", "Phone code"]:
                exp = f"{Fore.WHITE}{Style.BRIGHT}{key:<8}{Style.RESET_ALL}\t {info}"
            else:
                exp = f"{Fore.WHITE}{Style.BRIGHT}{key:<8}{Style.RESET_ALL}\t {tran} ({info})"
            details.append(exp)
        else:
            details.append(
                f"{Fore.WHITE}{Style.BRIGHT}{key:<8}{Style.RESET_ALL}\t {info}"
            )
    return details


def get_loc_info(lat: float, lon: float) -> list:
    url = f"https://amap.com/service/regeo?longitude={lon}&latitude={lat}"
    try:
        res = requests.get(url)
        if res.status_code == 200:
            js = res.json()
        else:
            print(f"Error, can't get information:  HTTP status {res.status_code}")
            exit()
    except Exception as e:
        print(f"Error: {e}")
        exit()
    if js["status"] == "1":
        return translate(js["data"])


def print_urls(coords, url_list):
    [
        print(f"{url['name']}: {url['url'].format(lat=coords.lat, lon=coords.lon)}")
        for url in url_list
    ]


def to_from_baidu(
    lat: float,
    lon: float,
    r: bool,
    wgs: bool = False,
    gcj: bool = False,
    bd: bool = False,
    i: bool = False,
) -> None:
    coords_bd = coords_gcj = coords_wgs = None
    Coords = collections.namedtuple("Coords", "lat lon")
    if r:
        if bd is True:
            print(
                f"{Fore.WHITE}{Style.BRIGHT}Conversion from BD-09 (Baidu) coordinates {lat}, {lon}{Style.RESET_ALL}"
            )
            coords_wgs = prcoords.bd_wgs_bored((lat, lon))
            coords_gcj = prcoords.bd_gcj_bored((lat, lon))
        elif gcj is True:
            print(
                f"{Fore.WHITE}{Style.BRIGHT}Conversion from GCJ-02 coordinates {lat}, {lon}{Style.RESET_ALL}"
            )
            coords_wgs = prcoords.gcj_wgs_bored((lat, lon))
            coords_gcj = Coords(lat, lon)

        print(
            f"\n{Fore.GREEN}{Style.BRIGHT}-> WGS-84 coordinates: {coords_wgs.lat}, {coords_wgs.lon}{Style.RESET_ALL}"
        )
        print_urls(coords_wgs, urls.to_wgs)

        print(
            f"\n{Fore.GREEN}{Style.BRIGHT}-> GCJ-02 coordinates: {coords_gcj.lat}, {coords_gcj.lon}{Style.RESET_ALL}"
        )
        print_urls(coords_gcj, urls.to_gcj)
        print()

        if i:
            infos = get_loc_info(coords_gcj.lat, coords_gcj.lon)
            [print(info) for info in infos]
            print()

    else:

        if wgs is True:
            print(
                f"{Fore.WHITE}{Style.BRIGHT}Conversion from WGS-84 coordinates {lat}, {lon}{Style.RESET_ALL}"
            )
            coords_bd = prcoords.wgs_bd((lat, lon))
            coords_gcj = prcoords.wgs_gcj((lat, lon))

        elif gcj is True:
            print(
                f"{Fore.WHITE}{Style.BRIGHT}Conversion from GCJ-02 coordinates {lat}, {lon}{Style.RESET_ALL}"
            )
            coords_bd = prcoords.gcj_bd((lat, lon))
            coords_gcj = Coords(lat, lon)

        print(
            f"\n{Fore.GREEN}{Style.BRIGHT}-> BD-09 coordinates: {coords_bd.lat}, {coords_bd.lon}{Style.RESET_ALL}"
        )
        print_urls(coords_bd, urls.wgs_to_bd)

        print(
            f"\n{Fore.GREEN}{Style.BRIGHT}-> GCJ-02 coordinates: {coords_gcj.lat}, {coords_gcj.lon}{Style.RESET_ALL}"
        )
        print_urls(coords_gcj, urls.wgs_to_gcj)
        print()

        if i:
            infos = get_loc_info(coords_gcj.lat, coords_gcj.lon)
            [print(info) for info in infos]
            print()


def main():
    parser = argparse.ArgumentParser(
        description=intro, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "latitude",
        type=float,
        help="latitude in decimal degrees, e.g. 39.882276480039216",
    )
    parser.add_argument(
        "longitude",
        type=float,
        help="longitude in decimal degrees, e.g. 116.40670177974461",
    )
    parser.add_argument(
        "-wgs", help="coordinates come from WGS-84", action="store_true"
    )
    parser.add_argument(
        "-gcj", help="coordinates come from GCJ-02", action="store_true"
    )
    parser.add_argument("-bd", help="coordinates come from BD-09", action="store_true")
    parser.add_argument(
        "-r",
        action="store_true",
        help="convert from BD-09 or GCJ-02 to WGS-84",
    )
    parser.add_argument(
        "-i",
        help="fetch and translate online basic information about the location",
        action="store_true",
    )

    args = parser.parse_args()
    print(intro)
    if args.wgs is False and args.gcj is False and args.r is False:
        print(
            "\nOne of the arguments --sat or --road is required tp convert to Baidu:\n"
            "--sat if the coordinates come from the satellite view\n"
            "--road if the coordinates come from the roadmap view",
            end="\n\n",
        )
        exit()

    to_from_baidu(
        args.latitude, args.longitude, args.r, args.wgs, args.gcj, args.bd, args.i
    )


if __name__ == "__main__":
    main()
