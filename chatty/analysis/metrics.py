from chatty.analysis.analysis import (vocab, emojis, avg_message_words,
                                      avg_message_chars, longest_message,
                                      pct_sentiment)
from chatty.analysis.preprocessing import filter_stopwords, stem, filter_english


class Metric:

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


MESSAGE_COUNT = Metric('Message Count',
                       lambda messages, sentiment: len(messages),
                       "{:,}")

WORD_COUNT = Metric('Word Count',
                    lambda messages, sentiment: sum(len(x) for x in messages),
                    "{:,}")

AVG_WORD_COUNT = Metric('Avg Message Word Count',
                        lambda messages, sentiment: avg_message_words(
                            messages),
                        "{0:.2f}")

AVG_WORD_COUNT_WO_STOP = Metric('Avg Message Word Count (w/o Stop Words)',
                                lambda messages, sentiment:
                                avg_message_words(filter_stopwords(messages)),
                                "{0:.2f}")

AVG_CHAR_COUNT = Metric('Avg Message Character Count',
                        lambda messages, sentiment: avg_message_chars(
                            messages),
                        "{0:.2f}")

AVG_CHAR_COUNT_WO_STOP = Metric('Avg Message Character Count (w/o Stop Words)',
                                lambda messages, sentiment:
                                avg_message_chars(filter_stopwords(messages)),
                                "{0:.2f}")

LONGEST_MESSAGE = Metric('Longest Message',
                         lambda messages, sentiment: longest_message(messages),
                         "{:,}")

DISTINCT_WORDS = Metric('Distinct Words',
                        lambda messages, sentiment: len(vocab(messages)),
                        "{:,}")

DISTINCT_STEMS = Metric('Distinct Stems',
                        lambda messages, sentiment: len(vocab(stem(messages))),
                        "{:,}")

DISTINCT_ENGLISH_WORDS = \
    Metric('Distinct English Words',
           lambda messages, sentiment: len(vocab(filter_english(messages))),
           "{:,}")

DISTINCT_EMOJIS = Metric('Distinct Emojis',
                         lambda messages, sentiment: len(emojis(messages)),
                         "{:,}")

EMOJI_COUNT = \
    Metric('Emoji Count',
           lambda messages, sentiment: sum(x[1] for x in emojis(messages)),
           "{:,}")

PCT_NEGATIVE_SENTIMENT = \
    Metric('Pct Negative Sentiment',
           lambda messages, sentiment:
           pct_sentiment(sentiment, lambda x: x < -.5),
           "{0:.0f}%")

PCT_POSITIVE_SENTIMENT = \
    Metric('Pct Positive Sentiment',
           lambda messages, sentiment:
           pct_sentiment(sentiment, lambda x: x > .5),
           "{0:.0f}%")

DEFAULT_METRICS = [
    MESSAGE_COUNT,
    WORD_COUNT,
    AVG_WORD_COUNT,
    AVG_WORD_COUNT_WO_STOP,
    AVG_CHAR_COUNT,
    AVG_CHAR_COUNT_WO_STOP,
    LONGEST_MESSAGE,
    DISTINCT_WORDS,
    DISTINCT_STEMS,
    DISTINCT_ENGLISH_WORDS,
    DISTINCT_EMOJIS,
    EMOJI_COUNT,
    PCT_NEGATIVE_SENTIMENT,
    PCT_POSITIVE_SENTIMENT
]
