from .analysis import vocab, emojis, avg_message_words, avg_message_chars, \
                      longest_message, pct_sentiment
from .preprocessing import filter_stopwords, stem, filter_english

class Metric(object):

    def __init__(self, name, calc,
                 format_str=f"{0}"):
        self.name = name
        self.calc = calc
        self.format_str = format_str

    def compute(self, messages, sentiment):
        return self.calc(messages, sentiment)

    def formatted(self, messages, sentiment):
        val = self.compute(messages, sentiment)
        return self.format_str.format(val)

DEFAULT_METRICS = [
    Metric('Message Count',
           lambda messages, sentiment: len(messages),
           "{:,}"),
    Metric('Word Count',
           lambda messages, sentiment: sum(len(x) for x in messages),
           "{:,}"),
    Metric('Avg Message Word Count',
           lambda messages, sentiment: avg_message_words(messages),
           "{0:.2f}"),
    Metric('Avg Message Word Count (w/o Stop Words)',
           lambda messages, sentiment: \
               avg_message_words(filter_stopwords(messages)),
           "{0:.2f}"),
    Metric('Avg Message Character Count',
           lambda messages, sentiment: avg_message_chars(messages),
           "{0:.2f}"),
    Metric('Avg Message Character Count (w/o Stop Words)',
           lambda messages, sentiment:
           avg_message_chars(filter_stopwords(messages)),
           "{0:.2f}"),
    Metric('Longest Message',
           lambda messages, sentiment: \
               longest_message(messages),
           "{:,}"),
    Metric('Distinct Words',
           lambda messages, sentiment: len(vocab(messages)),
           "{:,}"),
    Metric('Distinct Stems',
           lambda messages, sentiment: len(vocab(stem(messages))),
           "{:,}"),
    Metric('Distinct English Words',
           lambda messages, sentiment: len(vocab(filter_english(messages))),
           "{:,}"),
    Metric('Distinct Emojis',
           lambda messages, sentiment: len(emojis(messages)),
           "{:,}"),
    Metric('Emoji Count',
           lambda messages, sentiment: sum(x[1] for x in emojis(messages)),
           "{:,}"),
    Metric('Pct Negative Sentiment',
           lambda messages, sentiment: \
               pct_sentiment(sentiment, lambda x: x < -.5),
           "{0:.0f}%"),
    Metric('Pct Positive Sentiment',
           lambda messages, sentiment: \
               pct_sentiment(sentiment, lambda x: x > .5),
           "{0:.0f}%")
]
