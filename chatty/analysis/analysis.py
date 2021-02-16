from collections import Counter
from itertools import chain

import emoji
import grapheme
import numpy as np
import pandas as pd


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from chatty.analysis.preprocessing import (filter_alpha, filter_stopwords,
                                           sentences)


def frequency(items):
    counts = Counter(items)
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)


def vocab(messages):
    return frequency(chain.from_iterable(
        filter_alpha(filter_stopwords(messages))))


def emojis(messages):
    def helper():
        for message in messages:
            if isinstance(message, list):
                message = ''.join(message)
            try:
                for grapheme_cluster in grapheme.graphemes(message):
                    if grapheme_cluster in emoji.UNICODE_EMOJI_ENGLISH or \
                            len(grapheme_cluster) > 1:
                        yield grapheme_cluster
            except:  # pylint: disable=bare-except
                pass

    return frequency(helper())


def sentiment(messages):
    analyzer = SentimentIntensityAnalyzer()
    negative = []
    neutral = []
    positive = []
    compound = []
    for sentence in chain.from_iterable(sentences(messages)):
        res = analyzer.polarity_scores(sentence)
        negative.append(res['neg'])
        neutral.append(res['neu'])
        positive.append(res['pos'])
        compound.append(res['compound'])

    return pd.DataFrame({
        'negative': negative,
        'neutral': neutral,
        'positive': positive,
        'compound': compound
    })


def avg_message_words(messages):
    return np.mean(np.array([len(x) for x in messages]))


def avg_message_chars(messages):
    char_counts = [sum([len(x) for x in message]) for message in messages]
    return np.mean(np.array(char_counts))


def longest_message(messages):
    if not messages:
        return 0
    return max(len(x) for x in messages)


def pct_sentiment(sentiment_df, comp):
    compound = sentiment_df['compound']
    return 100*compound[comp(compound)].count()/len(compound)


def emoji_table(messages):
    return pd.DataFrame(emojis(messages), columns=['Emoji', 'Frequency'])


def vocab_table(messages):
    df = pd.DataFrame(vocab(messages), columns=['Word', 'Frequency'])
    df.set_index('Word', inplace=True)
    return df


def word_count_table(messages):
    return pd.DataFrame([len(x) for x in messages], columns=['Word Count'])
