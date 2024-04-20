"""
Analyzer the sentiments within a video, potentially classifying as
positive, negative, toxic, concerning etc
"""

def analyze_attitudes(self):
        """
        Analyze the transcript to determine the attitudes expressed.
        You can use sentiment analysis techniques to categorize the attitude.
        """
        # You can use a library like TextBlob or spaCy for sentiment analysis
        from textblob import TextBlob
        
        text = self.extract_text()
        blob = TextBlob(text)
        sentiment = blob.sentiment
        
        if sentiment.polarity > 0:
            attitude = "Positive"
        elif sentiment.polarity < 0:
            attitude = "Negative"
        else:
            attitude = "Neutral"
        
        return attitude