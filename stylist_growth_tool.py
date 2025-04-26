import streamlit as st
import requests
import time
import datetime

# ---- CONFIGURATION ----
ZAPIER_WEBHOOK_URL = "https://hooks.zapier.com/hooks/catch/22679760/2p6zm30/"  # Your Zapier webhook URL here

# ---- SUGGESTIONS ENGINE ----
def generate_growth_plan(data):
    suggestions = []

    # 1. Pricing Strategy
    if data["womens_cut_price"] < 45:
        suggestions.append("Increase your women's haircut price to at least $50 to better align with local STL metro averages and signal premium service.")

    if data["mens_cut_price"] < 30:
        suggestions.append("Raise your men's haircut price to $30–$40 depending on your experience level and clientele, to boost perceived value.")

    # 2. Service Expansion
    if data["balayage_offered"] == "No":
        suggestions.append("Consider adding balayage to your services at an introductory rate of around $125 to attract new high-ticket clients.")

    if data["extensions_offered"] == "No" and data["years_experience"] >= 2:
        suggestions.append("Get certified in hair extensions within 6 months — extension services in STL average $400–$800 and can double your revenue potential.")

    # 3. Marketing Focus
    if data["instagram_posts"] < 4:
        suggestions.append("Post at least 5x/week on Instagram showcasing transformations and behind-the-scenes work to build momentum.")

    if data["tiktok_posts"] < 2:
        suggestions.append("Start posting 2+ TikToks per week using trending sounds to reach new clients locally.")

    if data["facebook_posts"] < 2:
        suggestions.append("Repurpose your Instagram posts for Facebook at least 2–3 times a week to capture a different local audience.")

    # 4. Client Retention
    if data["first_time_retention"] < 50:
        suggestions.append("Implement a first-visit rebooking incentive (e.g., free deep conditioner if they rebook same day) to improve retention.")

    if data["no_show_rate"] > 10:
        suggestions.append("Introduce a 24-hour cancellation policy with a 50% fee to reduce no-shows and protect your schedule.")

    # 5. Retail & Reviews
    if data["retail_sales_percent"] < 10:
        suggestions.append("Recommend 1 product at checkout consistently — it can add an extra 10–15% in revenue without additional work.")

    if data["review_rating"] < 4.5:
        suggestions.append("Actively request Google reviews after appointments to strengthen your online reputation and local SEO.")

    return suggestions[:5]  # Return only the top 5 suggestions

# ---- FRONTEND ----
st.title("Stylist Growth Strategy Generator ✨")
st.write("Answer a few quick questions to get a hyper-specific growth plan tailored to you and your business. Enter your email to receive a copy!")

# Form Inputs
with st.form("growth_form"):
    st.subheader("Your Info")
    name = st.text_input("Your Name")
    email = st.text_input("Email Address")
    business_type = st.selectbox("Which best describes your business model?", ["Commission Stylist", "Booth Renter", "Salon Owner", "Mobile Stylist"])
    years_experience = st.slider("How many years have you been doing hair?", 0, 50, 1)

    st.subheader("Service Offerings & Pricing")
    balayage_offered = st.radio("Do you offer Balayage?", ["Yes", "No"])
    partial_foil_offered = st.radio("Do you offer Partial Foil Highlights?", ["Yes", "No"])
    full_foil_offered = st.radio("Do you offer Full Foil Highlights?", ["Yes", "No"])
    color_correction_offered = st.radio("Do you offer Color Correction?", ["Yes", "No"])
    extensions_offered = st.radio("Do you offer Hair Extensions?", ["Yes", "No"])

    womens_cut_price = st.number_input("Women's Haircut Price ($)", min_value=0.0)
    mens_cut_price = st.number_input("Men's Haircut Price ($)", min_value=0.0)

    st.subheader("Social Media Presence")
    instagram_posts = st.number_input("Instagram posts per week", min_value=0)
    instagram_engagement = st.slider("Instagram engagement rate (%)", 0, 100, 0)
    facebook_posts = st.number_input("Facebook posts per week", min_value=0)
    facebook_engagement = st.slider("Facebook engagement rate (%)", 0, 100, 0)
    tiktok_posts = st.number_input("TikTok posts per week", min_value=0)
    tiktok_engagement = st.slider("TikTok engagement rate (%)", 0, 100, 0)

    st.subheader("Client Flow Metrics")
    first_time_retention = st.slider("First-time client retention rate (%)", 0, 100, 0)
    rebooking_rate = st.slider("Rebooking at checkout rate (%)", 0, 100, 0)
    new_clients_monthly = st.number_input("New clients gained per month", min_value=0)
    referral_program = st.radio("Do you have a referral program?", ["Yes", "No"])

    st.subheader("Retail Sales & No-Show Management")
    retail_sales_percent = st.slider("Retail product sales (% of total revenue)", 0, 100, 0)
    no_show_rate = st.slider("No-show rate (%)", 0, 100, 0)

    st.subheader("Client Satisfaction")
    review_rating = st.slider("Average client review rating (stars)", 1.0, 5.0, 5.0, step=0.1)

    submitted = st.form_submit_button("Generate Growth Plan 🚀")

if submitted:
    with st.spinner("Generating your personalized growth plan..."):
        # Bundle data
        survey_data = {
            "name": name,
            "email": email,
            "business_type": business_type,
            "years_experience": years_experience,
            "balayage_offered": balayage_offered,
            "partial_foil_offered": partial_foil_offered,
            "full_foil_offered": full_foil_offered,
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
            "timestamp": datetime.datetime.now().isoformat(),
        }

        # Send data to Zapier
        try:
            requests.post(ZAPIER_WEBHOOK_URL, json=survey_data)
        except Exception as e:
            st.warning(f"Failed to send data to database: {e}")

        # Generate suggestions
        growth_plan = generate_growth_plan(survey_data)

        time.sleep(1)  # Just to let the spinner run briefly

    # Display Results
    st.success(f"✅ Growth plan generated! (A copy will be emailed soon to {email}.)")

    st.subheader("Your Top Action Steps:")
    for i, suggestion in enumerate(growth_plan, 1):
        st.markdown(f"**{i}.** {suggestion}")





