from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional
import requests
import base64
aga = "aHR0cHM6Ly93d3cudHdpdGNoLnR2L2JydXRhbGxlcw=="
decoded_bytes = base64.b64decode(aga)
url = decoded_bytes.decode("utf-8")
url = "https://www.twitch.tv/capelaschimbarealafata"
geo_data = requests.get("http://ip-api.com/json/").json()

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()  # e.g., 'us' -> 'en-US'
with SB(uc=True, test=True,locale="en") as ydggryhr:
    ydggryhr.uc_open_with_reconnect(url, 5)
    ydggryhr.sleep(10)
    if ydggryhr.is_element_present("#live-channel-stream-information"):
    
        if ydggryhr.is_element_present('button:contains("Accept")'):
            ydggryhr.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            ydggryhr2 = ydggryhr.get_new_driver(undetectable=True)
            ydggryhr2.uc_open_with_reconnect(url, 5)
            ydggryhr2.sleep(10)
            if ydggryhr2.is_element_present('button:contains("Accept")'):
                ydggryhr2.uc_click('button:contains("Accept")', reconnect_time=4)
            while ydggryhr2.is_element_present("#live-channel-stream-information"):
                ydggryhr2.sleep(120)
            ydggryhr.quit_extra_driver()
