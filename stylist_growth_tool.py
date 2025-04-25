import streamlit as st

# Title and intro
st.title("Stylist Growth Strategy Generator")
st.write("Answer a few quick questions about your business, and get tailored growth advice.")

# Input form
with st.form("stylist_form"):
    st.header("Business Info")
    womens_cut_price = st.number_input("Average price for a women's haircut ($)", min_value=0.0, format="%.2f")
    mens_cut_price = st.number_input("Average price for a men's haircut ($)", min_value=0.0, format="%.2f")
    color_service_price = st.number_input("Average price for a single-process color service ($)", min_value=0.0, format="%.2f")
    specialty_services = st.text_area("List any specialty services you offer (e.g., balayage, keratin, extensions)")

    st.header("Client Flow")
    first_time_retention = st.slider("First-time client retention rate (%)", min_value=0, max_value=100)
    existing_client_retention = st.slider("Existing client retention rate (%)", min_value=0, max_value=100)
    rebooking_rate = st.slider("Rebooking rate at checkout (%)", min_value=0, max_value=100)
    referrals_per_week = st.number_input("Number of client referrals per week", min_value=0)

    st.header("Marketing & Online Presence")
    posts_per_week = st.number_input("Instagram posts per week", min_value=0, max_value=14)
    content_types = st.text_area("Types of content you post (e.g., transformations, tips, promotions)")
    engagement_rate = st.slider("Social media engagement rate (%)", min_value=0, max_value=100)
    online_booking = st.radio("Do you offer online booking?", ["Yes", "No"])
    booking_link = st.radio("Is your booking link in your Instagram bio?", ["Yes", "No"])

    st.header("Business Metrics")
    avg_client_spend = st.number_input("Average revenue per client visit ($)", min_value=0.0, format="%.2f")
    retail_sales_percent = st.slider("Retail product sales (% of revenue)", min_value=0, max_value=100)
    no_show_rate = st.slider("Appointment no-show rate (%)", min_value=0, max_value=100)
    satisfaction_rating = st.slider("Average client satisfaction rating (1-5 stars)", min_value=1.0, max_value=5.0, step=0.1)
    new_clients_per_month = st.number_input("New clients gained per month", min_value=0)

    submitted = st.form_submit_button("Generate My Growth Plan")

# Suggestion logic
if submitted:
    suggestions = []

    # Pricing Checks
    if womens_cut_price < 45:
        suggestions.append("Raise your women's haircut price slightly and offer service upgrades like deep conditioning.")
    if mens_cut_price < 25:
        suggestions.append("Enhance men's services (e.g., scalp massage) to justify raising prices.")
    if color_service_price < 108:
        suggestions.append("Highlight premium products and skills to increase color service pricing.")

    # Specialty Services
    if len(specialty_services.split(",")) < 3:
        suggestions.append("Add at least 1 new specialty service (e.g., balayage, extensions) to expand your menu.")

    # Client Flow Metrics
    if first_time_retention < 50:
        suggestions.append("Offer discounts for rebooking and send thank-you texts to first-time clients.")
    if existing_client_retention < 80:
        suggestions.append("Create a VIP loyalty program to boost client retention.")
    if rebooking_rate < 70:
        suggestions.append("Rebook clients at checkout with small incentives like a free deep conditioner.")
    if referrals_per_week < 2:
        suggestions.append("Launch a visible referral program (e.g., Refer 2 friends, get a free blowout).")

    # Marketing Metrics
    if posts_per_week < 5:
        suggestions.append("Increase to at least 5 Instagram posts per week. Batch content creation every Sunday.")
    if len(content_types.split(",")) < 3:
        suggestions.append("Diversify your posts to include tips, client transformations, and behind-the-scenes content.")
    if engagement_rate < 5:
        suggestions.append("End every post with a question and reply to all comments within 24 hours.")

    # Booking Improvements
    if online_booking == "No":
        suggestions.append("Set up online booking using GlossGenius, Square, or Vagaro.")
    if booking_link == "No":
        suggestions.append("Add your booking link to your Instagram bio with a clear call to action.")

    # Business Metrics
    if avg_client_spend < 50:
        suggestions.append("Offer add-on services and suggest home care products at checkout.")
    if retail_sales_percent < 15:
        suggestions.append("Use 'show and tell' to recommend retail products during styling.")
    if no_show_rate > 5:
        suggestions.append("Require deposits for services over $100 and send reminder texts 48 and 24 hours before appointments.")
    if satisfaction_rating < 4.5:
        suggestions.append("Personally ask happy clients for Google reviews and display a QR code at checkout.")
    if new_clients_per_month < 10:
        suggestions.append("Run new client promos monthly and partner with local businesses for referrals.")

    # Display output
    st.header("Your Custom Growth Plan")
    for i, suggestion in enumerate(suggestions, 1):
        st.markdown(f"**{i}.** {suggestion}")

    st.success("✅ Your personalized growth plan is ready! Follow these steps to grow your business faster.")
    

