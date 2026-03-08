import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# -----------------------------------
# Load API Key from .env
# -----------------------------------
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("❌ API Key not found. Please check your .env file.")
    st.stop()

# -----------------------------------
# Configure Gemini
# -----------------------------------
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    model_name="models/gemini-flash-latest",
    generation_config={
        "temperature": 0.4,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 2048
    }
)

# -----------------------------------
# Background Styling (CLEAN + SAFE)
# -----------------------------------
def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background: radial-gradient(circle at top left, #1f2933, #020617);
            color: #ffffff;
        }

        h1, h2, h3, label {
            color: #e5e7eb !important;
        }

        input, textarea {
            background-color: #020617 !important;
            color: #ffffff !important;
            border-radius: 10px !important;
        }

        button {
            background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
            color: white !important;
            border-radius: 12px !important;
            padding: 0.6rem 1.4rem !important;
            font-weight: 600 !important;
        }

        /* 🔥 REMOVE "Press Enter to apply" (Streamlit caption/help text) */
        div[data-testid="stTextInput"] small,
        div[data-testid="stTextInput"] div[data-testid="stCaption"],
        div[data-testid="stNumberInput"] small,
        div[data-testid="stNumberInput"] div[data-testid="stCaption"] {
            display: none !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# -----------------------------------
# Generate Travel Itinerary
# -----------------------------------
def generate_itinerary(destination, days, nights,):
    prompt = f"""
    Create a detailed and clean travel itinerary.

    Destination: {destination}
    Duration: {days} days and {nights} nights
    Include:
    - Day-wise plan
    - Attractions
    - Food recommendations
    - Travel tips
    """

    response = model.generate_content(prompt)
    return response.text

# -----------------------------------
# Streamlit UI
# -----------------------------------
st.set_page_config(
    page_title="Travel Itinerary Generator",
    page_icon="🌍",
    layout="centered"
)

set_background()

st.title("🌍 Travel Itinerary Generator")
st.divider()

destination = st.text_input("📍 Enter your destination")
days_input = st.text_input("📅 Number of days", value="1")
nights_input = st.text_input("🌙 Number of nights", value="0")
st.divider()

if st.button("✨ Generate Itinerary"):
    try:
        days = int(days_input)
        nights = int(nights_input)

        if days <= 0 or nights < 0:
            st.warning("Days must be > 0 and nights ≥ 0.")
        elif not destination.strip():
            st.warning("Please enter a destination.")
        else:
            with st.spinner("🧠 Planning your journey..."):
                itinerary = generate_itinerary(destination, days, nights,)

            st.text_area(
                "📖 Generated Travel Itinerary",
                itinerary,
                height=300
            )
    except ValueError:
        st.error("Please enter valid numeric values for days and nights.")
