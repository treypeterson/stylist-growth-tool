import streamlit as st
import requests
from datetime import datetime

# Zapier Webhook URL (replace with your real URL)
zapier_webhook_url = "https://hooks.zapier.com/hooks/catch/22679760/2p6zm30/"

st.title("Stylist Growth Strategy Generator")
st.write("Answer a few quick questions to get a hyper-specific growth plan tailored to you and your business. Enter your email to receive a copy!")

# User Information
st.header("Your Info")
name = st.text_input("Your Name")
email = st.text_input("Email Address")
# Username feature turned OFF for now

business_type = st.selectbox(
    "Which best describes your business model?",
    ["Commission Stylist", "Booth Rental", "Salon Owner", "Mobile Stylist", "Other"]
)
years_experience = st.slider("How many years have you been doing hair?", 0, 50, 1)

# Services
st.header("Service Offerings & Pricing")
balayage_offered = st.radio("Do you offer Balayage?", ("Yes", "No"))
balayage_price = None
if balayage_offered == "Yes":
    balayage_price = st.number_input("If yes, current Balayage price ($)", min_value=0.0)

partial_foil_offered = st.radio("Do you offer Partial Foil Highlights?", ("Yes", "No"))
partial_foil_price = None
if partial_foil_offered == "Yes":
    partial_foil_price = st.number_input("If yes, current Partial Foil price ($)", min_value=0.0)

full_foil_offered = st.radio("Do you offer Full Foil Highlights?", ("Yes", "No"))
full_foil_price = None
if full_foil_offered == "Yes":
    full_foil_price = st.number_input("If yes, current Full Foil price ($)", min_value=0.0)

color_correction_offered = st.radio("Do you offer Color Correction?", ("Yes", "No"))
extensions_offered = st.radio("Do you offer Hair Extensions?", ("Yes", "No"))

# Pricing
st.header("Haircut Pricing")
womens_cut_price = st.number_input("Women's Haircut Price ($)", min_value=0.0)
mens_cut_price = st.number_input("Men's Haircut Price ($)", min_value=0.0)

# Social Media
st.header("Social Media Presence")
instagram_posts = st.number_input("Instagram posts per week", min_value=0)
instagram_engagement = st.slider("Instagram engagement rate (%)", 0, 100)

facebook_posts = st.number_input("Facebook posts per week", min_value=0)
facebook_engagement = st.slider("Facebook engagement rate (%)", 0, 100)

tiktok_posts = st.number_input("TikTok posts per week", min_value=0)
tiktok_engagement = st.slider("TikTok engagement rate (%)", 0, 100)

# Client Metrics
st.header("Client Flow Metrics")
first_time_retention = st.slider("First-time client retention rate (%)", 0, 100)
rebooking_rate = st.slider("Rebooking at checkout rate (%)", 0, 100)
new_clients_monthly = st.number_input("New clients gained per month", min_value=0)
referral_program = st.radio("Do you have a referral program?", ("Yes", "No"))

# Retail and No-shows
st.header("Retail Sales & No-Show Management")
retail_sales_percent = st.slider("Retail product sales (% of total revenue)", 0, 100)
no_show_rate = st.slider("No-show rate (%)", 0, 100)

# Client Reviews
st.header("Client Satisfaction")
review_rating = st.slider("Average client review rating (stars)", 1.0, 5.0, step=0.1)

# Submit Button
if st.button("Generate Growth Plan"):
    st.success(f"✅ Growth plan generated! (The emailing feature will be added soon for {email}.)")
    st.write("Here’s what you submitted:")
    
    data = {
        "timestamp": str(datetime.now()),
        "name": name,
        "email": email,
        "business_type": business_type,
        "years_experience": years_experience,
        "balayage_offered": balayage_offered,
        "balayage_price": balayage_price,
        "partial_foil_offered": partial_foil_offered,
        "partial_foil_price": partial_foil_price,
        "full_foil_offered": full_foil_offered,
        "full_foil_price": full_foil_price,
        "color_correction_offered": color_correction_offered,
        "extensions_offered": extensions_offered,
        "womens_cut_price": womens_cut_price,
        "mens_cut_price": mens_cut_price,
        "instagram_posts": instagram_posts,
        "instagram_engagement": instagram_engagement,
        "facebook_posts": facebook_posts,
        "facebook_engagement": facebook_engagement,
        "tiktok_posts": tiktok_posts,
        "tiktok_engagement": tiktok_engagement,
        "first_time_retention": first_time_retention,
        "rebooking_rate": rebooking_rate,
        "new_clients_monthly": new_clients_monthly,
        "referral_program": referral_program,
        "retail_sales_percent": retail_sales_percent,
        "no_show_rate": no_show_rate,
        "review_rating": review_rating,
    }
    
    st.json(data)

    # --- Send to Zapier Webhook ---
    try:
        response = requests.post(zapier_webhook_url, json=data)
        if response.status_code == 200:
            st.success("🎯 Your data was successfully sent to the database!")
        else:
            st.error(f"⚠️ Error sending data. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"⚠️ Exception occurred: {e}")



