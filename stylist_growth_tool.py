import streamlit as st
import requests
import datetime

st.set_page_config(page_title="Stylist Growth Strategy Generator")
st.title("Stylist Growth Strategy Generator")
st.write("Answer a few quick questions to get a hyper-specific growth plan tailored to you and your business. Enter your email to receive a copy!")

# --- User Info ---
with st.form(key='survey_form'):
    st.header("Your Info")
    name = st.text_input("Your Name")
    email = st.text_input("Email Address")
    business_type = st.selectbox("Which best describes your business model?", ["Commission Stylist", "Booth Renter", "Salon Owner", "Independent Suite Owner"])
    years_experience = st.slider("How many years have you been doing hair?", 0, 50, 1)

    # --- Service Offerings ---
    st.header("Service Offerings & Pricing")
    balayage_offered = st.radio("Do you offer Balayage?", ("Yes", "No"))
    if balayage_offered == "Yes":
        balayage_price = st.number_input("Current Balayage Price ($)", min_value=0.0, step=1.0)
    else:
        balayage_price = None

    partial_foil_offered = st.radio("Do you offer Partial Foil Highlights?", ("Yes", "No"))
    if partial_foil_offered == "Yes":
        partial_foil_price = st.number_input("Current Partial Foil Price ($)", min_value=0.0, step=1.0)
    else:
        partial_foil_price = None

    full_foil_offered = st.radio("Do you offer Full Foil Highlights?", ("Yes", "No"))
    if full_foil_offered == "Yes":
        full_foil_price = st.number_input("Current Full Foil Price ($)", min_value=0.0, step=1.0)
    else:
        full_foil_price = None

    color_correction_offered = st.radio("Do you offer Color Correction?", ("Yes", "No"))
    extensions_offered = st.radio("Do you offer Hair Extensions?", ("Yes", "No"))

    # --- Haircut Pricing ---
    st.header("Haircut Pricing")
    womens_cut_price = st.number_input("Women's Haircut Price ($)", min_value=0.0, step=1.0)
    mens_cut_price = st.number_input("Men's Haircut Price ($)", min_value=0.0, step=1.0)

    # --- Social Media Presence ---
    st.header("Social Media Presence")
    instagram_posts = st.number_input("Instagram posts per week", min_value=0)
    instagram_engagement = st.slider("Instagram engagement rate (%)", 0, 100, 0)
    facebook_posts = st.number_input("Facebook posts per week", min_value=0)
    facebook_engagement = st.slider("Facebook engagement rate (%)", 0, 100, 0)
    tiktok_posts = st.number_input("TikTok posts per week", min_value=0)
    tiktok_engagement = st.slider("TikTok engagement rate (%)", 0, 100, 0)

    # --- Client Flow Metrics ---
    st.header("Client Flow Metrics")
    first_time_retention = st.slider("First-time client retention rate (%)", 0, 100, 0)
    rebooking_rate = st.slider("Rebooking at checkout rate (%)", 0, 100, 0)
    new_clients_monthly = st.number_input("New clients gained per month", min_value=0)
    referral_program = st.radio("Do you have a referral program?", ("Yes", "No"))

    # --- Retail & No-Show Management ---
    st.header("Retail Sales & No-Show Management")
    retail_sales_percent = st.slider("Retail product sales (% of total revenue)", 0, 100, 0)
    no_show_rate = st.slider("No-show rate (%)", 0, 100, 0)

    # --- Client Satisfaction ---
    st.header("Client Satisfaction")
    review_rating = st.slider("Average client review rating (stars)", 1.0, 5.0, 5.0, step=0.1)

    submit_button = st.form_submit_button(label='Generate My Growth Plan')

if submit_button:
    with st.spinner('Analyzing your business and creating custom growth recommendations...'):

        # --- Prepare data for Zapier ---
        payload = {
            "name": name,
            "email": email,
            "timestamp": str(datetime.datetime.now()),
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
            "review_rating": review_rating
        }

        # --- Send to Zapier ---
        requests.post("https://hooks.zapier.com/hooks/catch/22679760/2p6zm30/", json=payload)

        # --- Generate Suggestions ---
        suggestions = []

        if balayage_offered == "No":
            suggestions.append("Since you're not currently offering balayage but have {} years experience, adding balayage services could unlock $1k–$2k/month in additional revenue.".format(years_experience))

        if instagram_posts < 3 or instagram_engagement < 5:
            suggestions.append("Since your Instagram posting and engagement are low, prioritize posting 4-5x weekly with client transformations to boost visibility and bookings.")

        if rebooking_rate < 60:
            suggestions.append("Since your rebooking rate is {}%, immediately implement rebooking scripts at checkout to raise rebooking to 70%+. This stabilizes your monthly income.").format(rebooking_rate)

        if new_clients_monthly < 8:
            suggestions.append("Because you're gaining fewer than 8 new clients monthly, we recommend a $5/day Facebook and Instagram ad spend targeting women 25–45 in your city.")

        if no_show_rate > 10:
            suggestions.append("Since your no-show rate is {}%, implement automated confirmation texts 48 and 24 hours before appointments.".format(no_show_rate))

        if retail_sales_percent < 10:
            suggestions.append("Because retail sales are under 10% of your revenue, start recommending 2 specific products per appointment to boost revenue.")

        if mens_cut_price < 35:
            suggestions.append("Given your market and experience level, raising your men's haircut price to $35–$45 would better match local market rates.")

        if review_rating < 4.5:
            suggestions.append("Since your average review rating is {} stars, create a QR code linked to your Google reviews page and offer clients a $5 retail discount for leaving a 5-star review.").format(review_rating)

        if first_time_retention < 50:
            suggestions.append("With a first-time retention rate under 50%, offer a 'Welcome Back' bonus for rebooking within 6 weeks (ex: free deep conditioning treatment).")

        # --- Display Final Plan ---
        st.success("✅ Your Personalized Growth Plan")

        for idx, rec in enumerate(suggestions[:10], 1):
            st.write(f"**{idx}.** {rec}")

        st.markdown("---")
        st.info("These are your **most urgent recommendations** based on your current business data. Implement them and check back in 60–90 days for a new customized plan!")






