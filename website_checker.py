import requests

websites = ["https://google.com", "https://github.com", "https://nonexistent.xyz"]

for site in websites:
    try:
        r = requests.get(site)
        print(f"{site} is online. Status code: {r.status_code}")
    except:
        print(f"{site} is offline.")
