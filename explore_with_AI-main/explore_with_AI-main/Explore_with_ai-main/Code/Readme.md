# 🌍 Travel Itinerary Generator (Gemini AI + Streamlit)

An AI-powered web application that generates personalized travel itineraries
based on user inputs such as destination, number of days, nights, and interests.
The application uses **Google Gemini Flash (latest)** and is deployed using
**Streamlit** with a clean dark-themed UI.

---

## ✨ Features

- 🌐 Personalized AI-generated travel itineraries
- 🤖 Powered by Google Gemini (`models/gemini-flash-latest`)
- 🔐 Secure API key management using `.env`
- 🎨 Modern dark UI with Streamlit
- 🧳 Day-wise travel plan
- 🍽️ Local food & attraction recommendations
- 🚫 No unwanted UI elements (`+ / -`, “Press Enter to apply” removed)
- ⚡ Fast and lightweight application

---

## 🧠 Tech Stack

- **Frontend / Backend**: Streamlit
- **AI Model**: Google Gemini Flash (Latest)
- **Programming Language**: Python
- **Environment Variables**: python-dotenv

---

## 📁 Project Structure

│
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
└── .env # Environment variables (API key)


---

## 📦 Requirements

All dependencies are listed in `requirements.txt`:


Install them using:

pip install -r requirements.txt

## Create a .env file in the project root directory:
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

## How to run the application
Run the Streamlit app using:

streamlit run travel.py
