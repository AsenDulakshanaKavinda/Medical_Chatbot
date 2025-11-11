from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from chatbot.src.generate import Generate  # import your class

app = Flask(__name__, template_folder="templates")
CORS(app)  # allow frontend JS calls (if served elsewhere)

generator = Generate()  # load your model once


@app.route("/")
def index():
    return render_template("index.html")  # serves the chat UI


@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")
        history = data.get("history", [])

        # use your LangChain chain to generate response
        chain = generator._setup_chain()
        response = chain.invoke({"input": user_message})

        reply = response["answer"] if isinstance(response, dict) else str(response)
        return jsonify({"reply": reply})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"reply": "Sorry, an internal error occurred."}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
