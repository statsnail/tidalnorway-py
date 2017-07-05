#!/usr/bin/env python3

# tidalnorway-py
# Quick and dirty scraper for water level data in Norway
# Simple version for water level only: http://api.sehavniva.no/tidepos_en.html
# More fancy one is here: http://api.sehavniva.no/tideapi_en.html
# Garten Position 63.642022, 9.498116
# A full request for one day looks like this:
# http://api.sehavniva.no/tideapi.php?lat=63.642022&lon=9.498116&fromtime=2017-07-05T00%3A00&totime=2017-07-06T00%3A00&datatype=tab&refcode=cd&place=&file=&lang=en&interval=10&dst=1&tzone=1&tide_request=locationdata

from lxml import html
from bs4 import BeautifulSoup
import requests
import datetime
from pytz import timezone

if __name__ == '__main__':
    print("tidalnorway-py supposed to be a class in the future")

    #t = timezone(settings.TIME_ZONE).localize(datetime.now()).replace(microsecond=0)
    current_time_utc_iso = datetime.datetime.utcnow().replace(microsecond=0).isoformat()
    print("Current datetime =", current_time_utc_iso)
    print("### RESPONSE FROM SERVER ###")
    #page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
    lat = "63.642022"
    lon = "9.498116"
    fromtime = "2017-07-05T00:00"
    totime = "2017-07-06T00:00"
    datatype = "tab"
    refcode = "cd"
    place = ""
    file = ""
    lang = "en"
    interval = "10"
    dst = "1"
    tzone = "0"
    tide_request = "locationdata"
    
    payload = {'lat': lat, 'lon': lon, 'fromtime': fromtime, 'totime': totime, 'datatype': datatype, 'refcode': refcode, 'place': place, 'file': file, 'lang': lang, 'interval': interval, 'dst': dst, 'tzone': tzone, 'tide_request': tide_request}

    page = requests.get("http://api.sehavniva.no/tideapi.php", params=payload)
    soup = BeautifulSoup(page.content, 'lxml-xml')
    print(soup.prettify())
