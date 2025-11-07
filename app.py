import streamlit as st
import requests

st.set_page_config(page_title="🌦️ Weather App", page_icon="🌤️", layout="centered")

st.title("🌦️ Weather App by Yar Muhammad")
st.write("Enter a city name below to check the current weather 🌍")

# Input box for city
city = st.text_input("City name", "")

# OpenWeatherMap API setup
api_key = "7055d7ad4fb2f20cd481886345bba8a6"  # Replace with your OpenWeatherMap API key
base_url = "https://api.openweathermap.org/data/2.5/weather"

if city:
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        icon = data["weather"][0]["icon"]

        st.subheader(f"🌤️ Weather in {city.title()}")
        st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png")
        st.write(f"**Temperature:** {temp}°C")
        st.write(f"**Humidity:** {humidity}%")
        st.write(f"**Description:** {weather}")

    elif response.status_code == 404:
        st.error("❌ City not found. Please enter a valid city name.")
    else:
        st.error("⚠️ Unable to fetch weather data at the moment.")
else:
    st.info("👆 Please type a city name to begin.")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit and OpenWeatherMap API")
