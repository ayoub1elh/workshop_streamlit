"""
Sentiment Analysis Module
Handles text analysis using TextBlob
"""

from textblob import TextBlob


def analyze_sentiment(text: str) -> dict:
    """
    Analyze the sentiment of a text using TextBlob.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        dict: Contains 'score', 'sentiment', and 'emoji'
    """
    blob = TextBlob(text)
    score = blob.sentiment.polarity
    
    # Classify the sentiment
    if score > 0.1:
        sentiment = 'POSITIF'
        emoji = '😊'
    elif score < -0.1:
        sentiment = 'NÉGATIF'
        emoji = '😞'
    else:
        sentiment = 'NEUTRE'
        emoji = '😐'
    
    return {
        'score': score,
        'sentiment': sentiment,
        'emoji': emoji
    }


def get_sentiment_color(score: float) -> str:
    """
    Get the color associated with a sentiment score.
    
    Args:
        score (float): The sentiment score
        
    Returns:
        str: The color name ('success', 'error', 'info')
    """
    if score > 0.1:
        return 'success'
    elif score < -0.1:
        return 'error'
    else:
        return 'info'
