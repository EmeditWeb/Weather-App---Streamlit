import streamlit as st
import requests

# Load API key securely from Streamlit secrets
key = st.secrets["general"]["key"]

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        return temp, weather_desc.capitalize(), humidity, wind_speed
    else:
        return None

# Streamlit App 
st.set_page_config(page_title="Weather Notifier", page_icon="🌦")

st.markdown(
    """
    <style>
.stTextInput {
        border: 2px solid black;
        box-shadow: 2px 2px 10px black;
        padding: 10px;
}
.green-box {
        background-color: #d4edda;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        font-weight: bold;
}
.footer {
        text-align: center;
        font-weight: bold;
        margin-top: 20px;
}
.pro-version {
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        margin-top: 20px;
}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Weather Notifier App")

with st.form("weather_form"):
    name = st.text_input("Enter your name", key="name")
    city = st.text_input("Enter city name", key="city")
    submit_button = st.form_submit_button("Get Weather")

if submit_button:
    weather_info = get_weather(city)

    if weather_info:
        temp, weather_desc, humidity, wind_speed = weather_info

        st.markdown(f'<div class="green-box">{city} Weather</div>', unsafe_allow_html=True)
        st.write(f"**Temperature:** {temp}°C")
        st.write(f"**Weather:** {weather_desc}")
        st.write(f"**Humidity:** {humidity}%")
        st.write(f"**Wind Speed:** {wind_speed} m/s")

        if temp> 30:
            st.success(f"Hey {name}, it's quite hot in {city} today 🌞.")
        elif temp < 15:
            st.success(f"Hey {name}, it's chilly in {city}, dress warm 🥶.")
        else:
            st.success(f"Hey {name}, the weather in {city} seems pleasant 😊.")
    else:
        st.error("City not found! Please try again.")

st.markdown('<div class="pro-version">Pro Version: <a href="https://emedit-wapi.netlify.app" target="_blank">Click Here</a></div>', unsafe_allow_html=True)

st.markdown('<div class="footer">Built by Emedit | Powered by Streamlit</div>', unsafe_allow_html=True)
