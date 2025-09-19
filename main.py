from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# OpenAI API key (Railway पर Environment Variable में डालना)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/angel", methods=["POST"])
def angel():
    data = request.json
    user_msg = data.get("payload", {}).get("payload", {}).get("text", "")

    if not user_msg:
        return jsonify({"success": False})

    # OpenAI से reply बनवाना
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Angel, a positive and helpful WhatsApp problem solver bot."},
            {"role": "user", "content": user_msg}
        ],
        max_tokens=200
    )

    angel_reply = response.choices[0].message["content"].strip()

    return jsonify({
        "success": True,
        "response": angel_reply
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
