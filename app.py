from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "02a79ea344ff4d9f8e075406250310"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"{BASE_URL}?key={API_KEY}&q={city}&aqi=no"
            response = requests.get(url)
            data = response.json()
            if "error" in data:
                error = data["error"]["message"]
            else:
                weather_data = {
                    "city": data["location"]["name"],
                    "country": data["location"]["country"],
                    "temperature": data["current"]["temp_c"],
                    "condition": data["current"]["condition"]["text"],
                    "icon": data["current"]["condition"]["icon"],
                    "humidity": data["current"]["humidity"],
                    "wind": data["current"]["wind_kph"],
                }
    return render_template("index.html", weather=weather_data, error=error)


if __name__ == "__main__":
    app.run(debug=True)
