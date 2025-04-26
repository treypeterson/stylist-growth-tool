import streamlit as st

# Title and intro
st.title("Stylist Growth Strategy Generator")
st.write("Answer a few quick questions about your business, and get a hyper-specific, STL-metro-specific growth plan.")

# Input form
with st.form("stylist_form"):
    st.header("Service Offerings & Pricing")
    balayage_offered = st.radio("Do you offer Balayage?", ["Yes", "No"])
    if balayage_offered == "Yes":
        balayage_price = st.number_input("Current Balayage price ($)", min_value=0.0, format="%.2f")

    partial_foil_offered = st.radio("Do you offer Partial Foil Highlights?", ["Yes", "No"])
    if partial_foil_offered == "Yes":
        partial_foil_price = st.number_input("Current Partial Foil price ($)", min_value=0.0, format="%.2f")

    full_foil_offered = st.radio("Do you offer Full Foil Highlights?", ["Yes", "No"])
    if full_foil_offered == "Yes":
        full_foil_price = st.number_input("Current Full Foil price ($)", min_value=0.0, format="%.2f")

    color_correction_offered = st.radio("Do you offer Color Correction?", ["Yes", "No"])
    extensions_offered = st.radio("Do you offer Hair Extensions?", ["Yes", "No"])

    st.header("Haircut Pricing")
    womens_cut_price = st.number_input("Women's Haircut price ($)", min_value=0.0, format="%.2f")
    mens_cut_price = st.number_input("Men's Haircut price ($)", min_value=0.0, format="%.2f")

    st.header("Social Media Presence")
    instagram_posts = st.number_input("Instagram posts per week", min_value=0)
    instagram_engagement = st.slider("Instagram engagement rate (%)", 0, 100)

    facebook_posts = st.number_input("Facebook posts per week", min_value=0)
    facebook_engagement = st.slider("Facebook engagement rate (%)", 0, 100)

    tiktok_posts = st.number_input("TikTok posts per week", min_value=0)
    tiktok_engagement = st.slider("TikTok engagement rate (%)", 0, 100)

    st.header("Client Flow")
    first_time_retention = st.slider("First-time client retention rate (%)", 0, 100)
    rebooking_rate = st.slider("Rebooking rate at checkout (%)", 0, 100)
    new_clients_per_month = st.number_input("New clients gained per month", min_value=0)
    referral_program = st.radio("Do you have a referral program?", ["Yes", "No"])

    st.header("Retail Sales & No-Show Management")
    retail_sales_percent = st.slider("Retail product sales (% of revenue)", 0, 100)
    no_show_rate = st.slider("No-show rate (%)", 0, 100)

    st.header("Client Satisfaction")
    review_rating = st.slider("Average client review rating (stars)", 1.0, 5.0, step=0.1)

    submitted = st.form_submit_button("Generate My Growth Plan")

# Suggestion logic
if submitted:
    suggestions = []

    st.header("Your Custom Growth Plan")

    # Services
    if balayage_offered == "No":
        suggestions.append("Offer Balayage at an intro price of $125 for first 10 clients, then adjust to market rate $160–$190.")
    elif balayage_price < 160:
        suggestions.append("Raise Balayage pricing to $160–$190 to align with STL metro market rates.")

    if partial_foil_offered == "No":
        suggestions.append("Add Partial Foil Highlights service. Intro price $90 for 5 clients, then raise to $110–$130 standard.")
    elif partial_foil_price < 100:
        suggestions.append("Raise Partial Foil pricing to $110–$130 range for competitive STL standards.")

    if full_foil_offered == "No":
        suggestions.append("Add Full Foil Highlights at an intro price of $130, then standardize pricing at $140–$170.")
    elif full_foil_price < 140:
        suggestions.append("Raise Full Foil pricing to $140–$170 for STL metro market competitiveness.")

    if color_correction_offered == "No":
        suggestions.append("Add Color Correction service. Start consults free, then $85–$100/hr based on complexity.")

    if extensions_offered == "No":
        suggestions.append("Begin Hair Extensions certification. Offer model installs at discount; full pricing $350–$800 depending on method.")

    # Haircut Pricing
    if womens_cut_price < 50:
        suggestions.append("Raise Women's Haircut price to $50–$75 depending on your skill and target market.")
    if mens_cut_price < 30:
        suggestions.append("Raise Men's Haircut price to $30–$50 range. Introduce a Maintenance Club Membership option.")

    # Client Retention
    if first_time_retention < 50:
        suggestions.append("Offer a 'Welcome Back' perk (free deep conditioner or $10 off) for first-time rebookings within 6 weeks.")
    if rebooking_rate < 70:
        suggestions.append("Use a rebooking script at checkout and aim for 70%+ same-day rebooking.")

    # New Client Acquisition
    if new_clients_per_month < 10:
        suggestions.append("Launch New Client Offer (15% off) and run a $5/day boosted ad on Instagram + Facebook for 14 days.")

    if referral_program == "No":
        suggestions.append("Create Referral Program: Refer a friend = $10 off for both referrer and new client.")

    # Social Media Presence
    if instagram_posts < 5:
        suggestions.append("Post at least 5x per week on Instagram: 2 client transformations, 1 haircare tip, 1 behind-the-scenes, 1 promo.")
    if instagram_engagement < 5:
        suggestions.append("End every Instagram post with a question to boost engagement.")

    if facebook_posts < 3:
        suggestions.append("Post at least 3x per week on Facebook — cross-promote Instagram content if needed.")
    if facebook_engagement < 3:
        suggestions.append("Boost key Facebook posts with $5 to $10 ads targeted to local area.")

    if tiktok_posts < 3:
        suggestions.append("Post at least 3 TikToks per week showcasing transformations, funny trends, or hair tips.")
    if tiktok_engagement < 3:
        suggestions.append("Use trending sounds and hashtags on TikTok to increase local visibility.")

    # Retail Sales
    if retail_sales_percent < 15:
        suggestions.append("Recommend 1–2 retail products to every client. Promote bundles (Buy 2, Get 10% Off).")

    # No-Show Management
    if no_show_rate > 5:
        suggestions.append("Enforce 30–50% deposit for bookings over $100. Send 48hr + 24hr reminder texts.")

    # Client Satisfaction
    if review_rating < 4.5:
        suggestions.append("Create a QR code linking to Google Reviews and offer $5 off for leaving a review.")

    for idx, suggestion in enumerate(suggestions, 1):
        st.markdown(f"**{idx}.** {suggestion}")

    st.success("✅ Your hyper-specific growth plan is ready! Execute these steps to build sustainable success.")
