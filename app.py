from flask import Flask, render_template, request
from predict import predict_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = confidence = None
    text = ""

    if request.method == "POST":
        text = request.form["message"]
        result, confidence = predict_text(text)

    return render_template(
        "index.html",
        result=result,
        confidence=confidence,
        text=text
    )

if __name__ == "__main__":
    app.run(debug=True)
