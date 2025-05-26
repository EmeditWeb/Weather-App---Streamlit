import streamlit as st
import requests

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=67c742dfdc14a695f3640d8379406c68&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]

        if temp> 30:
            return f"Hey {name}, it's quite hot in {city} today!"
        elif temp < 15:
            return f"Hey {name}, it's chilly in {city}, dress warm!"
        else:
            return f"Hey {name}, the weather in {city} seems pleasant."
    else:
        return "City not found! Please try again."

# Streamlit UI
st.set_page_config(page_title="Weather Notifier", page_icon="🌦")

st.markdown(
    """
    <style>
.stTextInput {
        border: 2px solid black;
        box-shadow: 2px 2px 10px black;
        padding: 10px;
}
.footer {
        text-align: center;
        font-weight: bold;
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

# User Input Form
with st.form("weather_form"):
    name = st.text_input("Enter your name", key="name")
    city = st.text_input("Enter city name", key="city")
    submit_button = st.form_submit_button("Get Weather")

if submit_button:
    message = get_weather(city)
    st.success(message)

# Pro Version Section
st.markdown('<div class="pro-version">Pro Version: <a href="https://emedit-wapi.netlify.app" target="_blank">Click Here</a></div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Built by Emedit | Powered by Streamlit</div>', unsafe_allow_html=True)
