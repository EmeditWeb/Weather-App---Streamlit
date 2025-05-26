# Weather Notifier App

## Description
The Weather Notifier App is a simple and interactive web application built using Streamlit. It allows users to enter their name and city to fetch real-time weather data. The app provides temperature, weather description, humidity, and wind speed, and gives contextual insights based on the temperature.

*Features*
- Retrieves live weather data for any city using OpenWeatherMap API.
- Provides user-friendly feedback based on temperature conditions.
- Displays the temperature, weather conditions, humidity, and wind speed.
- Stylish UI with bordered input fields and shadow effects.
- Includes a link to the *Pro Version* upgrade.
- Footer credits: *Built by Emedit | Powered by Streamlit*.

---

## Deployment Instructions

*1. Install Dependencies*
Ensure Python and `pip` are installed, then install the required packages:

```bash
pip install streamlit requests
```

---

*2. Setup API Key*
1. Get an API key from *OpenWeatherMap* ([https://home.openweathermap.org/users/sign_up](https://home.openweathermap.org/users/sign_up)).
2. Create a `config.json` file in the project directory:

```json
{
    "API_KEY": "your_api_key_here"
}
```

3. Make sure `config.json` is added to `.gitignore` to prevent exposure.

---

*3. Run Locally*
Execute the Streamlit app locally:

```bash
streamlit run weather_notifier.py
```

This opens the app in your browser.

---

*4. Deploy on Streamlit Community Cloud*
1. Push your code to a *GitHub repository*.
2. Go to *Streamlit Community Cloud* ([https://share.streamlit.io](https://share.streamlit.io)).
3. Click *"Deploy an app"* and link your GitHub repository.
4. Select `weather_notifier.py` and deploy.

---

*5. Alternative Deployment on Cloud Servers*
If deploying on *AWS, Heroku, or Render*:
- Set up Python and Streamlit on the server.
- Run `streamlit run weather_notifier.py`.
- Configure *Nginx/Gunicorn* for production use.

---

Pro Version :
🔗 [Visit Here](https://emedit-wapi.netlify.app)

---

Credits
Built by Emedit | Powered by Streamlit
