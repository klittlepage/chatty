from nltk import Text
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import sent_tokenize
from nltk.tokenize.casual import TweetTokenizer

from nltk.stem.porter import PorterStemmer

def normalize_messages(messages):
    tokenizer = TweetTokenizer(preserve_case=False)
    normalized_messages = []
    for message in messages:
        try:
            tokens = tokenizer.tokenize(message)
            text = [word.lower() for word in Text(tokens)]
            if text:
                normalized_messages.append(text)
        except TypeError:
            pass
    return normalized_messages

def stem(messages):
    stemmer = PorterStemmer()
    return [[stemmer.stem(word) for word in message] \
            for message in messages]

STOPWORDS = stopwords.words('english')
def filter_stopwords(messages, stopword_corpus=STOPWORDS):
    return [[word for word in message \
             if word not in stopword_corpus] \
            for message in messages]

def filter_english(messages):
    return [[word for word in message \
             if wordnet.synsets(word)] \
            for message in messages]

def filter_alpha(messages):
    return [[word for word in message if word.isalpha()] \
            for message in messages]

def sentences(messages):
    msg_sentences = []
    for message in messages:
        try:
            msg_sentences.append(sent_tokenize(message))
        except TypeError:
            pass
    return msg_sentences
