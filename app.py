import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

# Securely configure API key
GOOGLE_API_KEY = "AIzaSyDuLiCCvqZeHk9r0uxp-9ESdlwICyyR90U"
if not GOOGLE_API_KEY:
    st.error("⚠️Missing Google GenAI API key! Please set it in environment variables.⚠️")
    st.stop()

st.set_page_config(page_title="AI-Powered Travel Planner", page_icon="🌏", layout="wide")
# Function to retrieve AI-powered travel suggestions
def fetch_travel_recommendations(start, end):
    system_instruction = SystemMessage(
        content="You are a travel assistant AI. Provide travel options like flights, buses, trains, and taxis with details."
    )
    user_query = HumanMessage(
        content=f"I'm planning a trip from {start} to {end}. Suggest different travel modes, estimated costs, and travel tips."
    )

    # Initialize LLM with API key
    ai_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=GOOGLE_API_KEY)
    
    try:
        result = ai_model.invoke([system_instruction, user_query])
        return result.content
    except Exception as error:
        return f"❌Unable to retrieve travel options: {str(error)}"

# Streamlit UI Setup
st.title("🚂Smart Travel Planner with AI✈️")
st.write("Enter travel details to get the best AI-generated travel suggestions!")

# User Inputs
start_location = st.text_input("Source Location", placeholder="E.g. New Delhi")
destination_location = st.text_input("Destination", placeholder="E.g. Lucknow")

if st.button("Get Travel Suggestions"):
    if start_location.strip() and destination_location.strip():
        st.write(f"🔎Generating best travel routes from **{start_location}** to **{destination_location}**...🔍")
        travel_options = fetch_travel_recommendations(start_location, destination_location)
        st.write(travel_options)
    else:
        st.warning("⚠️Both source and destination must be provided!⚠️")

