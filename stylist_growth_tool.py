import streamlit as st
import datetime
import requests

# Title and intro
st.title("Stylist Growth Strategy Generator")
st.write("Answer a few quick questions to get a hyper-specific growth plan tailored to you and your business. Enter your email to receive a copy!")

# Form start
with st.form("growth_form"):
    st.header("Your Info")
    name = st.text_input("Your Name")
    email = st.text_input("Email Address")

    st.header("Business Details")
    business_type = st.selectbox("Which best describes your business model?", ["Commission Stylist", "Booth Rental", "Salon Owner", "Suite Owner", "Mobile Stylist"])
    years_experience = st.slider("How many years have you been doing hair?", 0, 50, 1)

    st.header("Service Offerings & Pricing")
    balayage_offered = st.radio("Do you offer Balayage?", ["Yes", "No"])
    balayage_price = None
    if balayage_offered == "Yes":
        balayage_price = st.number_input("Balayage Price ($)", min_value=0.0, step=1.0)

    partial_foil_offered = st.radio("Do you offer Partial Foil Highlights?", ["Yes", "No"])
    partial_foil_price = None
    if partial_foil_offered == "Yes":
        partial_foil_price = st.number_input("Partial Foil Price ($)", min_value=0.0, step=1.0)

    full_foil_offered = st.radio("Do you offer Full Foil Highlights?", ["Yes", "No"])
    full_foil_price = None
    if full_foil_offered == "Yes":
        full_foil_price = st.number_input("Full Foil Price ($)", min_value=0.0, step=1.0)

    color_correction_offered = st.radio("Do you offer Color Correction?", ["Yes", "No"])
    extensions_offered = st.radio("Do you offer Hair Extensions?", ["Yes", "No"])

    st.header("Haircut Pricing")
    womens_cut_price = st.number_input("Women's Haircut Price ($)", min_value=0.0, step=1.0)
    mens_cut_price = st.number_input("Men's Haircut Price ($)", min_value=0.0, step=1.0)

    st.header("Social Media Presence")
    instagram_posts = st.number_input("Instagram posts per week", min_value=0)
    instagram_engagement = st.slider("Instagram engagement rate (%)", 0, 100, 0)
    facebook_posts = st.number_input("Facebook posts per week", min_value=0)
    facebook_engagement = st.slider("Facebook engagement rate (%)", 0, 100, 0)
    tiktok_posts = st.number_input("TikTok posts per week", min_value=0)
    tiktok_engagement = st.slider("TikTok engagement rate (%)", 0, 100, 0)

    st.header("Client Flow Metrics")
    first_time_retention = st.slider("First-time client retention rate (%)", 0, 100, 0)
    rebooking_rate = st.slider("Rebooking at checkout rate (%)", 0, 100, 0)
    new_clients_monthly = st.number_input("New clients gained per month", min_value=0)
    referral_program = st.radio("Do you have a referral program?", ["Yes", "No"])

    st.header("Retail Sales & No-Show Management")
    retail_sales_percent = st.slider("Retail product sales (% of total revenue)", 0, 100, 0)
    no_show_rate = st.slider("No-show rate (%)", 0, 100, 0)

    st.header("Client Satisfaction")
    review_rating = st.slider("Average client review rating (stars)", 1.0, 5.0, 5.0, step=0.1)

    submitted = st.form_submit_button("Generate Growth Plan 🚀")

# After form submission
if submitted:
    with st.spinner('Analyzing your business and crafting your personalized plan...'):
        # Collect all data into a dictionary
        submission_data = {
            "timestamp": datetime.datetime.now().isoformat(),
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

        # Send to Google Sheets via Zapier Webhook
        webhook_url = "https://hooks.zapier.com/hooks/catch/22679760/2p6zm30/"
        try:
            requests.post(webhook_url, json=submission_data)
        except:
            st.warning("Could not send data to Google Sheets. Please check your Zap.")

        # --- Suggestions Generation ---
        suggestions = []

        if balayage_offered == "Yes" and (balayage_price is None or balayage_price < 180):
            suggestions.append("Since you offer Balayage and your price is below market rate, raise it to $180–$220 depending on your skill level and local demand.")

        if extensions_offered == "Yes":
            suggestions.append("Since you offer extensions, create a VIP Extension Membership to boost recurring revenue and loyalty.")

        if first_time_retention < 50:
            suggestions.append("Since your first-time retention rate is low at {}%, implement a new client follow-up system and loyalty incentives.".format(first_time_retention))

        if rebooking_rate < 70:
            suggestions.append("Since your rebooking rate is {}%, immediately implement rebooking scripts at checkout to raise rebooking to 70%+. This stabilizes your monthly income.".format(rebooking_rate))

        if new_clients_monthly < 5:
            suggestions.append("Since you're gaining fewer than 5 new clients per month, run a $5/day local Facebook and Instagram ad targeting women 25-45 nearby.")

        if retail_sales_percent < 10:
            suggestions.append("Since retail sales are under 10%, start recommending 1-2 products per client and create bundle promotions (Buy 2, Get 10% off).")

        if no_show_rate > 10:
            suggestions.append("Since your no-show rate is high ({}%), implement strict 24-hour cancellation policies and require a card-on-file.".format(no_show_rate))

        if instagram_posts < 3:
            suggestions.append("Since you're posting less than 3x/week on Instagram, aim for at least 5 high-quality posts weekly showing transformations, tips, and testimonials.")

        if review_rating < 4.5:
            suggestions.append("Since your client review rating is below 4.5 stars, actively request reviews from your happiest clients and set a goal to reach a 4.8 average.")

        if tiktok_posts < 2 and tiktok_engagement < 5:
            suggestions.append("Since TikTok engagement is low, post at least 3 short, fun videos weekly using trending sounds related to hair transformations.")

        # --- Output ---
        st.success("✅ Growth plan generated for {}! We've also emailed a copy to {} (if email automation is active).".format(name, email))
        st.subheader("Your Personalized Suggestions:")

        if suggestions:
            for suggestion in suggestions:
                st.write("- " + suggestion)
            st.markdown("✨ These are your most urgent opportunities for fast growth. Revisit and update your survey soon to unlock new, more advanced suggestions!")
        else:
            st.info("Your business looks fantastic already! Minor tweaks could still help you level up even further 🚀.")








