import unittest
from sentiment_model.sentiment import analyze_sentiment,format_output
from sentiment_model.errors.invalid_input_exception import InvalidInputException

class TestSentiment(unittest.TestCase):

    def test_positive_sentiment(self):
        result = analyze_sentiment("I love this product")
        self.assertEqual(result["sentiment"], "Positive")

    def test_negative_sentiment(self):
        result = analyze_sentiment("I hate this product")
        self.assertEqual(result["sentiment"], "Negative")

    def test_empty_input(self):
        with self.assertRaises(InvalidInputException):
          analyze_sentiment("")

    def test_format_output(self):
        result = format_output("I love this product")
        expected_result = {
            "text": "I love this product",
            "polarity": 0.5,
            "sentiment": "Positive",
            "confidence": 0.5
        }
        self.assertEqual(expected_result, result)
    
if __name__ == "__main__":
    unittest.main()
