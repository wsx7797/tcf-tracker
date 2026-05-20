import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

URL = "https://www.tcf.gov.tr/branslar/pilates/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
}

def send_whatsapp(msg):
    phone = os.getenv(905539851216)
    apikey = os.getenv(7654424)

    text = urllib.parse.quote(msg)

    url = f"https://api.callmebot.com/whatsapp.php?phone={phone}&text={text}&apikey={apikey}"
    requests.get(url)

r = requests.get(URL, headers=headers)

print("Status:", r.status_code)
print("Ankara var mı:", "Ankara" in r.text)

soup = BeautifulSoup(r.text, "html.parser")
