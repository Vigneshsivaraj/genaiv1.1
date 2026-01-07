from textblob import TextBlob
import json
from errors.invalid_input_exception import InvalidInputException

def analyze_sentiment(text) -> dict :
    if not text or not text.strip():
        raise InvalidInputException(f"Invalid Input {text}")
    blob = TextBlob(text)
    polarity = blob.polarity
    sentiment = ""
    if(polarity >= 0.1):
        sentiment = "Positive"
    elif(polarity < 0):
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "polarity" : polarity,
        "sentiment" : sentiment
    }

def format_output(text: str) -> dict:
    response = analyze_sentiment(text)

    polarity = round(response["polarity"], 2)

    return {
        "text": text,
        "polarity": polarity,
        "sentiment": response["sentiment"],
        "confidence": abs(polarity)
    }

def format_output_json(text: str) -> str:
    response = format_output(text)
    pretty_json = json.dumps(response,indent=4)
    return pretty_json
 