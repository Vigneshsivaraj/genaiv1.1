from flask import Flask,request,jsonify
import sentiment
from error_handlers import global_error_handler

app = Flask("Sentiment Detector")
global_error_handler(app)

@app.route("/health")
def getHealth():
    return "App is up",200

@app.route("/analyze",methods=['Post'])
def analyze_text():
    request_data = request.get_json()
    text = request_data["text"] if request_data else None
    return sentiment.format_output_json(text)


if __name__ == "__main__":
    app.run(debug=True)
