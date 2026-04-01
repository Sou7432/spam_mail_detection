from flask import Flask, render_template, request
from predict import predict_text
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    confidence = None
    text = ""

    if request.method == "POST":
        text = request.form.get("message", "")
        if text:
            result, confidence = predict_text(text)

    return render_template(
        "index.html",
        result=result,
        confidence=confidence,
        text=text
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT
    app.run(host="0.0.0.0", port=port)
