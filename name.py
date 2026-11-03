import os
import json
import urllib.request
import urllib.error

API_KEY = os.getenv("OTCHARTS_API_KEY")

if not API_KEY:
    raise SystemExit("OTCHARTS_API_KEY is missing")

url = "https://otcharts.com/v1/venues"

request = urllib.request.Request(
    url,
    headers={"Authorization": f"Bearer {API_KEY}"}
)

try:
    with urllib.request.urlopen(request, timeout=20) as response:
        data = json.loads(response.read().decode("utf-8"))

    print("OTCharts connection successful!")
    print(json.dumps(data, indent=2))

except urllib.error.HTTPError as error:
    print("API error:", error.code)
    print(error.read().decode("utf-8"))

except Exception as error:
    print("Connection failed:", error)
