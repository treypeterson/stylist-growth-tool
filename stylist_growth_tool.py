import streamlit as st

# ----------------- PAGE SETUP -----------------
st.set_page_config(page_title="Stylist Growth Strategy Generator", page_icon="✂️", layout="centered")

# ----------------- HEADER -----------------
st.title("Stylist Growth Strategy Generator")
st.write("Answer a few quick questions to get a hyper-specific growth plan tailored to you and your business. Enter your email to receive a copy!")

# ----------------- BASIC INFO -----------------
st.header("Your Info")
name = st.text_input("Your Name")
email = st.text_input("Email Address")
username = st.text_input("Create a Username")

business_type = st.selectbox("Which best describes your business model?", [
    "Booth Renter", "Commission Stylist", "Salon Owner", "Suite Renter", "Employee Stylist", "Other"
])

years_experience = st.slider("How many years have you been doing hair?", 0, 50, 1)

# ----------------- SERVICE OFFERINGS -----------------
st.header("Service Offerings & Pricing")

balayage = st.radio("Do you offer Balayage?", ("Yes", "No"))
if balayage == "Yes":
    balayage_price = st.number_input("Current Balayage Price ($)", min_value=0.0, format="%.2f")

partial_foil = st.radio("Do you offer Partial Foil Highlights?", ("Yes", "No"))
if partial_foil == "Yes":
    partial_foil_price = st.number_input("Current Partial Foil Price ($)", min_value=0.0, format="%.2f")

full_foil = st.radio("Do you offer Full Foil Highlights?", ("Yes", "No"))
if full_foil == "Yes":
    full_foil_price = st.number_input("Current Full Foil Price ($)", min_value=0.0, format="%.2f")

color_correction = st.radio("Do you offer Color Correction?", ("Yes", "No"))
extensions = st.radio("Do you offer Hair Extensions?", ("Yes", "No"))

# ----------------- HAIRCUT PRICING -----------------
st.header("Haircut Pricing")
womens_cut_price = st.number_input("Women's Haircut Price ($)", min_value=0.0, format="%.2f")
mens_cut_price = st.number_input("Men's Haircut Price ($)", min_value=0.0, format="%.2f")

# ----------------- SOCIAL MEDIA -----------------
st.header("Social Media Presence")
instagram_posts = st.number_input("Instagram posts per week", min_value=0)
instagram_engagement = st.slider("Instagram engagement rate (%)", 0, 100, 0)

facebook_posts = st.number_input("Facebook posts per week", min_value=0)
facebook_engagement = st.slider("Facebook engagement rate (%)", 0, 100, 0)

tiktok_posts = st.number_input("TikTok posts per week", min_value=0)
tiktok_engagement = st.slider("TikTok engagement rate (%)", 0, 100, 0)

# ----------------- CLIENT FLOW -----------------
st.header("Client Flow Metrics")
first_time_retention = st.slider("First-time client retention rate (%)", 0, 100, 0)
rebooking_rate = st.slider("Rebooking at checkout rate (%)", 0, 100, 0)
new_clients_monthly = st.number_input("New clients gained per month", min_value=0)

referral_program = st.radio("Do you have a referral program?", ("Yes", "No"))

# ----------------- RETAIL & NO-SHOWS -----------------
st.header("Retail Sales & No-Show Management")
retail_sales_percent = st.slider("Retail product sales (% of total revenue)", 0, 100, 0)
no_show_rate = st.slider("No-show rate (%)", 0, 100, 0)

# ----------------- CLIENT SATISFACTION -----------------
st.header("Client Satisfaction")
review_rating = st.slider("Average client review rating (stars)", 1.0, 5.0, 5.0, step=0.1)

# ----------------- DATA CAPTURE -----------------
answers = {
    "name": name,
    "email": email,
    "username": username,
    "business_type": business_type,
    "years_experience": years_experience,
    "balayage_offered": balayage,
    "balayage_price": balayage_price if balayage == "Yes" else None,
    "partial_foil_offered": partial_foil,
    "partial_foil_price": partial_foil_price if partial_foil == "Yes" else None,
    "full_foil_offered": full_foil,
    "full_foil_price": full_foil_price if full_foil == "Yes" else None,
    "color_correction_offered": color_correction,
    "extensions_offered": extensions,
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
    "review_rating": review_rating
}

# ----------------- BUTTONS -----------------
if st.button("Generate Growth Plan and Email Me"):
    if name and email and username:
        st.success(f"✅ Growth plan generated! (The emailing feature will be added soon for {email}.)")
        st.write("Here’s what you submitted:")
        st.json(answers)
    else:
        st.error("⚠️ Please complete your Name, Email, and Username before submitting.")


