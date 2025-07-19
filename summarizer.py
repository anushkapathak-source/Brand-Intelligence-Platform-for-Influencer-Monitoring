from nltk.tokenize import sent_tokenize
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.tokenizers import Tokenizer  # ✅ ADD THIS LINE
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

LANGUAGE = "english"
SENTENCES_COUNT = 5

def summarize_text(text, SENTENCES_COUNT=3):
    if not text or len(text.strip().split()) < 10:
        # Content too short for summarization
        return "Content too short to summarize."

    try:
        parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, SENTENCES_COUNT)
        result = " ".join(str(sentence) for sentence in summary)
        if not result:
            return "Summary not available."
        return result
    except Exception as e:
        return f"Summary generation failed: {e}"
