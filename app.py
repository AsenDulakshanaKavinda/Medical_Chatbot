from flask import Flask, render_template, request, jsonify
from chatbot.src.generate import Generate # import your generate() function

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    generator = Generate()
    user_input = request.json.get("message")  # get message from frontend
    response = generator.generate(user_input) # call your chatbot
    return jsonify({"answer": response})      # send JSON back

if __name__ == "__main__":
    app.run(debug=True)
