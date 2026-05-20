import requests
from bs4 import BeautifulSoup
import os
import urllib.parse
import time

URL = "https://www.tcf.gov.tr/branslar/pilates/"

def send_whatsapp(msg):
    phone = os.getenv(905539851216)
    apikey = os.getenv(7654424)

    text = urllib.parse.quote(msg)

    url = f"https://api.callmebot.com/whatsapp.php?phone={phone}&text={text}&apikey={apikey}"
    requests.get(url)

print("Bot başladı...")

while True:
    try:
        r = requests.get(URL)
        soup = BeautifulSoup(r.text, "html.parser")

        rows = soup.find_all("tr")

        for row in rows:
            text = row.get_text()

            if "Ankara" in text and "İncele" in text:
                send_whatsapp(f"🔥 Ankara kursu açıldı!\n{text}")

    except Exception as e:
        print("Hata:", e)

    time.sleep(30)
    
    
send_whatsapp("TEST MESAJI GELDİ 🚀")
