import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

URL = "https://www.tcf.gov.tr/branslar/pilates/"
def send_whatsapp(msg):
    phone = os.getenv(905539851216)
    apikey = os.getenv(7654424)

    text = urllib.parse.quote(msg)

    url = f"https://api.callmebot.com/whatsapp.php?phone={phone}&text={text}&apikey={apikey}"
    requests.get(url)

r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")

print("Ankara var mı:", "Ankara" in r.text)
print(r.text[:2000])

rows = soup.find_all("tr")

for row in rows:
    text = row.get_text()

    if "Ankara" in text and "İncele" in text:
        send_whatsapp("🔥 Ankara kursu açıldı!\n" + text)
