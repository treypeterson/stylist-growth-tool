import streamlit as st

# Title and intro
st.title("Stylist Growth Strategy Generator")
st.write("Answer a few quick questions about your business, and get tailored growth advice.")

# Input form
with st.form("stylist_form"):
    st.header("Business Info")
    followers = st.number_input("Instagram followers", min_value=0, step=100)
    posts_per_week = st.number_input("Instagram posts per week", min_value=0, max_value=14)
    location = st.text_input("City or ZIP code")
    hours_worked = st.number_input("Hours worked per week", min_value=0, max_value=100)

    st.header("Client Flow")
    new_clients = st.number_input("New clients per week", min_value=0)
    rebooking_rate = st.slider("Rebooking rate (%)", min_value=0, max_value=100)
    avg_price = st.number_input("Average service price ($)", min_value=0.0, format="%.2f")
    top_services = st.text_area("Top 1–3 services you offer")

    st.header("Marketing & Booking")
    online_booking = st.radio("Do you offer online booking?", ["Yes", "No"])
    link_in_bio = st.radio("Do you have a booking link in your Instagram bio?", ["Yes", "No"])
    referral_program = st.radio("Do you run a referral program?", ["Yes", "No"])

    st.header("Your Goals")
    income_goal = st.number_input("Monthly income goal ($)", min_value=0.0, format="%.2f")
    ideal_clients = st.text_area("What type of clients do you want more of?")

    submitted = st.form_submit_button("Generate My Growth Plan")

# Suggestion logic
if submitted:
    suggestions = []

    # Instagram advice
    if posts_per_week < 2:
        suggestions.append("Increase to at least 3 Instagram posts per week. Use client transformations and trending audio to boost engagement.")
    if followers < 500:
        suggestions.append("Focus on follower growth through reels and local hashtags. You’re in the early stage of your IG funnel.")

    # Booking
    if online_booking == "No":
        suggestions.append("Set up online booking through GlossGenius, Square, or Vagaro to streamline scheduling.")
    if link_in_bio == "No":
        suggestions.append("Add your booking link to your IG bio with a clear call to action. This small change can triple bookings.")

    # Rebooking
    if rebooking_rate < 50:
        suggestions.append("Encourage every client to rebook before they leave. Use scripts like: 'Let’s lock in your next appointment while you’re here.'")

    # Pricing
    if avg_price < 40:
        suggestions.append("Your average price is below industry norms. Consider increasing by $5 for your most booked service to reflect your value.")

    # Referral
    if referral_program == "No":
        suggestions.append("Start a simple referral program. Offer $10 off for both the referrer and the new client to encourage word-of-mouth growth.")

    # Display output
    st.header("Your Custom Growth Plan")
    for i, suggestion in enumerate(suggestions, 1):
        st.markdown(f"**{i}.** {suggestion}")
