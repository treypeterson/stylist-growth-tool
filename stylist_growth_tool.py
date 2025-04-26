# stylist_growth_tool.py

import datetime
import json
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

ZAPIER_WEBHOOK_URL = "https://hooks.zapier.com/hooks/catch/22679760/2p6zm30/"  # Your Zapier Webhook URL

def generate_suggestions(data):
    """Generate smart paragraph-style growth suggestions based on the survey answers."""
    suggestions = []

    # Analyze client flow metrics
    if data["first_time_retention"] < 60:
        suggestions.append(
            "Focus on improving your first-time client retention. Introduce a 'Welcome Back' incentive such as a complimentary deep conditioner for rebooking within 6 weeks."
        )
    if data["rebooking_rate"] < 70:
        suggestions.append(
            "Strengthen rebooking rates by using a consistent script at checkout offering 10% off their next service if booked today."
        )
    if data["new_clients_monthly"] < 5:
        suggestions.append(
            "Launch a 'New Client Special' and invest $5/day into targeted Instagram and Facebook ads to boost your visibility."
        )

    # Analyze service offerings and pricing
    if data["balayage_offered"] == "Yes" and data["balayage_price"] < 160:
        suggestions.append(
            "Your Balayage price is below the STL market average. Increase it gradually to $175–$190, marketing it as a 'Signature Balayage + Gloss + Bond Builder.'"
        )
    if data["womens_cut_price"] < 50:
        suggestions.append(
            "Consider raising your Women's Haircut price to $55–$65, especially if your retention and rebooking rates improve."
        )

    # Analyze social media presence
    if data["instagram_posts"] < 3 or data["instagram_engagement"] < 5:
        suggestions.append(
            "Post at least 5 times per week on Instagram and end each post with a question to double your engagement rate."
        )
    if data["tiktok_posts"] < 2:
        suggestions.append(
            "Expand onto TikTok with at least 2 videos per week using trending sounds to boost local visibility."
        )

    # Analyze retail and reviews
    if data["retail_sales_percent"] < 10:
        suggestions.append(
            "Introduce a simple 'Buy 2, Get 10% Off' retail bundle to boost retail sales and increase revenue."
        )
    if data["review_rating"] < 4.5:
        suggestions.append(
            "Create a QR code at checkout that links to your Google Reviews page and offer $5 off their next service for leaving a review."
        )

    # Limit to 3–5 most critical suggestions
    return suggestions[:5]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Capture form data
        form_data = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "business_type": request.form.get("business_type"),
            "years_experience": int(request.form.get("years_experience")),
            "balayage_offered": request.form.get("balayage_offered"),
            "balayage_price": float(request.form.get("balayage_price")) if request.form.get("balayage_offered") == "Yes" else None,
            "partial_foil_offered": request.form.get("partial_foil_offered"),
            "partial_foil_price": float(request.form.get("partial_foil_price")) if request.form.get("partial_foil_offered") == "Yes" else None,
            "full_foil_offered": request.form.get("full_foil_offered"),
            "full_foil_price": float(request.form.get("full_foil_price")) if request.form.get("full_foil_offered") == "Yes" else None,
            "color_correction_offered": request.form.get("color_correction_offered"),
            "extensions_offered": request.form.get("extensions_offered"),
            "womens_cut_price": float(request.form.get("womens_cut_price")),
            "mens_cut_price": float(request.form.get("mens_cut_price")),
            "instagram_posts": int(request.form.get("instagram_posts")),
            "instagram_engagement": int(request.form.get("instagram_engagement")),
            "facebook_posts": int(request.form.get("facebook_posts")),
            "facebook_engagement": int(request.form.get("facebook_engagement")),
            "tiktok_posts": int(request.form.get("tiktok_posts")),
            "tiktok_engagement": int(request.form.get("tiktok_engagement")),
            "first_time_retention": int(request.form.get("first_time_retention")),
            "rebooking_rate": int(request.form.get("rebooking_rate")),
            "new_clients_monthly": int(request.form.get("new_clients_monthly")),
            "referral_program": request.form.get("referral_program"),
            "retail_sales_percent": int(request.form.get("retail_sales_percent")),
            "no_show_rate": int(request.form.get("no_show_rate")),
            "review_rating": float(request.form.get("review_rating")),
        }

        # Send to Zapier
        payload = form_data.copy()
        payload["timestamp"] = datetime.datetime.utcnow().isoformat()
        requests.post(ZAPIER_WEBHOOK_URL, json=payload)

        # Generate smart suggestions
        suggestions = generate_suggestions(form_data)

        return render_template("results.html", suggestions=suggestions, name=form_data["name"], email=form_data["email"])

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)




