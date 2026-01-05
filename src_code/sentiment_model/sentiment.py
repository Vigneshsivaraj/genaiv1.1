from textblob import TextBlob

def analyze_sentiment(text) -> dict :
    if not text or not text.strip():
        return {
            "polarity" : 0,
            "sentiment" : "Neutral"
        }
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