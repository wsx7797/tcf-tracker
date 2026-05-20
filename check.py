import requests
from bs4 import BeautifulSoup
import os
import urllib.parse
import hashlib

URL = "https://www.tcf.gov.tr/branslar/pilates/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def send_whatsapp(msg):
    phone = os.getenv("905539851216")
    apikey = os.getenv("7654424")

    text = urllib.parse.quote(msg)

    url = f"https://api.callmebot.com/whatsapp.php?phone={phone}&text={text}&apikey={apikey}"
    requests.get(url)

r = requests.get(URL, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")

rows = soup.find_all("tr")

for row in rows:
    text = row.get_text().strip()

    if "Ankara" in text and "İncele" in text and "1. Kademe" in text:
        
        # benzersiz ID üret
        course_id = hashlib.md5(text.encode()).hexdigest()

        # GitHub cache gibi davran
        if os.path.exists(course_id):
            continue

        # yeni kurs
        send_whatsapp(f"🔥 YENİ ANKARA KURSU!\n{text}")

        # kaydet
        with open(course_id, "w") as f:
            f.write("sent")
