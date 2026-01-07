import unittest
import sentiment

class TestSentiment(unittest.TestCase):

    def test_positive_sentiment(self):
        result = sentiment.analyze_sentiment("I love this product")
        self.assertEqual(result["sentiment"], "Positive")

    def test_negative_sentiment(self):
        result = sentiment.analyze_sentiment("flood is coming to the city")
        self.assertEqual(result["sentiment"], "Negative")

    def test_empty_input(self):
        result = sentiment.analyze_sentiment("")
        self.assertEqual(result["sentiment"], "Neutral")

if __name__ == "__main__":
    unittest.main()
