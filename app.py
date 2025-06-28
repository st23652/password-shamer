from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from openai import OpenAI
import os
import urllib.parse

load_dotenv()
app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_prompt(password, level):
    tone = {
        "mild": "Roast this password politely but humorously.",
        "savage": "Roast this password with medium sarcasm and wit.",
        "nuclear": "Roast this password with absolutely brutal, over-the-top sarcasm and insults."
    }.get(level, "Roast this password humorously.")
    
    return f"""{tone}

Password: "{password}"

Roast:
"""

def roast_password(password, level):
    prompt = get_prompt(password, level)
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.9
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating roast: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        password = request.form.get("password", "")
        level = request.form.get("level", "mild")
        roast = roast_password(password, level)
        encoded_roast = urllib.parse.quote_plus(roast)
        return redirect(url_for("share", r=encoded_roast))
    return render_template("index.html")

@app.route("/share")
def share():
    roast = request.args.get("r", "")
    decoded = urllib.parse.unquote_plus(roast)
    full_link = request.url
    return render_template("share.html", roast=decoded, share_link=full_link)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
