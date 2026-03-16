import re

url=input("URL: ").strip()

if matches:=re.search(f"^https?://(?:www\.)?x\.com/([a-z,0-9,_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))