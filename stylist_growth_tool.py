import streamlit as st

# Title and intro
st.title("Stylist Growth Strategy Generator")
st.write("Answer a few quick questions about your business, and get a hyper-specific growth action plan.")

# Input form
with st.form("stylist_form"):
    st.header("Service Offerings & Pricing")
    balayage_offered = st.radio("Do you offer Balayage?", ["Yes", "No"])
    balayage_price = st.number_input("If yes, current Balayage price ($)", min_value=0.0, format="%.2f")

    partial_foil_offered = st.radio("Do you offer Partial Foil Highlights?", ["Yes", "No"])
    partial_foil_price = st.number_input("If yes, current Partial Foil price ($)", min_value=0.0, format="%.2f")

    full_foil_offered = st.radio("Do you offer Full Foil Highlights?", ["Yes", "No"])
    full_foil_price = st.number_input("If yes, current Full Foil price ($)", min_value=0.0, format="%.2f")

    color_correction_offered = st.radio("Do you offer Color Correction?", ["Yes", "No"])
    extensions_offered = st.radio("Do you offer Hair Extensions?", ["Yes", "No"])

    st.header("Haircut Pricing")
    womens_cut_price = st.number_input("Current price for Women's Haircut ($)", min_value=0.0, format="%.2f")
    mens_cut_price = st.number_input("Current price for Men's Haircut ($)", min_value=0.0, format="%.2f")

    st.header("Client Retention")
    first_time_retention = st.slider("First-time client retention rate (%)", 0, 100)
    rebooking_rate = st.slider("Rebooking at checkout rate (%)", 0, 100)

    st.header("New Client Acquisition")
    new_clients_per_month = st.number_input("New clients gained per month", min_value=0)
    referral_program = st.radio("Do you have a referral program?", ["Yes", "No"])

    st.header("Instagram Marketing")
    posts_per_week = st.number_input("Instagram posts per week", min_value=0, max_value=14)
    engagement_rate = st.slider("Instagram engagement rate (%)", 0, 100)

    st.header("Retail Product Sales")
    retail_sales_percent = st.slider("Retail product sales (% of total revenue)", 0, 100)

    st.header("No-Show Management")
    no_show_rate = st.slider("No-show rate (%)", 0, 100)

    st.header("Client Reviews")
    review_rating = st.slider("Average client review rating (stars)", 1.0, 5.0, step=0.1)

    submitted = st.form_submit_button("Generate My Growth Plan")

# Suggestion logic
if submitted:
    suggestions = []

    # Services
    if balayage_offered == "No":
        suggestions.append("Add Balayage service at $125 for first 10 clients, then raise to $160. Launch within 30 days.")
    elif balayage_price < 150:
        suggestions.append("Raise Balayage price by $15 immediately. Promote as 'Signature Balayage with Gloss + Bond Builder.'")

    if partial_foil_offered == "No":
        suggestions.append("Add Partial Foil service at $90 for first 5–8 clients, then raise to $110. Launch within 30 days.")
    elif partial_foil_price < 100:
        suggestions.append("Raise Partial Foil price by $15. Rebrand as 'Custom Dimensional Foiling.'")

    if full_foil_offered == "No":
        suggestions.append("Add Full Foil service at $130 intro price for first 5 clients, then $150.")
    elif full_foil_price < 140:
        suggestions.append("Raise Full Foil price by $15–$20. Market as 'Full Color Mapping.'")

    if color_correction_offered == "No":
        suggestions.append("List Color Correction service now. Offer free consultations for first 5 cases. Start at $85/hr.")

    if extensions_offered == "No":
        suggestions.append("Start certification in extensions within 60 days. Offer model installs with 20% discount.")

    # Haircut Pricing
    if womens_cut_price < 50:
        suggestions.append("Raise Women's Haircut price by $5 immediately. Add treatment upgrades for +$20 upsells.")

    if mens_cut_price < 30:
        suggestions.append("Raise Men's Haircut price by $5. Launch monthly 'Maintenance Club' membership option.")

    # Client Retention
    if first_time_retention < 50:
        suggestions.append("Launch Rebooking Reward (free deep conditioner if rebooked same day). Track offers on tally sheet.")

    if rebooking_rate < 70:
        suggestions.append("Use rebooking script at checkout 100% of the time. Offer 10% off next service if booked today.")

    # New Client Acquisition
    if new_clients_per_month < 10:
        suggestions.append("Launch New Client 15% Off Promo. Run boosted IG ad at $5/day for 2 weeks.")

    if referral_program == "No":
        suggestions.append("Launch 'Refer a Friend, Get $10 Off' program via text and social post.")

    # Instagram Marketing
    if posts_per_week < 5:
        suggestions.append("Post minimum 5x/week: 2 transformations, 1 tip, 1 behind-the-scenes, 1 promotion.")

    if engagement_rate < 5:
        suggestions.append("End posts with questions. Reply to comments within 2 hours to boost engagement.")

    # Retail Product Sales
    if retail_sales_percent < 15:
        suggestions.append("Recommend 1 product at every checkout. Launch 'Buy 2, Get 10% Off' bundle.")

    # No-Show Management
    if no_show_rate > 5:
        suggestions.append("Require 30–50% deposits for services over $100. Send 48 and 24-hour reminders.")

    # Client Reviews
    if review_rating < 4.5:
        suggestions.append("Create QR code linking to review page at checkout. Offer $5 off for leaving a review.")

    # Display output
    st.header("Your Custom Growth Plan")
    for i, suggestion in enumerate(suggestions, 1):
        st.markdown(f"**{i}.** {suggestion}")

    st.success("✅ Your personalized growth plan is ready! Follow these detailed steps to increase business.")