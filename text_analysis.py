from textblob import TextBlob
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords

# Ensure stopwords are downloaded
nltk.download('stopwords')

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def extract_topics(text, top_n=5):
    # Clean text and extract words
    words = re.findall(r'\b[a-z]{4,}\b', text.lower())

    # Use NLTK's stopwords
    stop_words = set(stopwords.words('english'))

    keywords = [word for word in words if word not in stop_words]
    most_common = Counter(keywords).most_common(top_n)
    return [word for word, freq in most_common]
