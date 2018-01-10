from itertools import chain

import matplotlib.pyplot as plt

from matplotlib.ticker import MaxNLocator
from tabulate import tabulate
from wordcloud import WordCloud

from .analysis.metrics import DEFAULT_METRICS
from .analysis.preprocessing import filter_stopwords

def full_title(title, title_suffix):
    if title_suffix:
        return "{0} ({1})".format(title, title_suffix)
    return title

def emoji_plot(emojis, title_suffix=None, ax=None,
               figsize=None):
    title = 'Most Frequently Used Emojis'
    ax = emojis.plot(kind='bar',
                     title=full_title(title, title_suffix),
                     ax=ax,
                     figsize=figsize)
    ax.set_xlabel('Emoji Index')
    ax.set_ylabel('Emoji Frequency')
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

def vocab_plot(vocab, title_suffix=None, ax=None,
               figsize=None):
    title = 'Most Frequently Used Words'
    ax = vocab.plot(kind='bar',
                    title=full_title(title, title_suffix),
                    ax=ax,
                    figsize=figsize)
    ax.set_xlabel('Word')
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(14)
    ax.set_ylabel('Word Usage Frequency')
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

def sentiment_plot(sentiment, title_suffix=None, ax=None,
                   figsize=None):
    title = 'Distribution of Message Sentiments'
    ax = sentiment.plot(kind='density',
                        title=full_title(title, title_suffix),
                        ax=ax,
                        figsize=figsize)
    ax.set_xlim([-1, 1])

def word_count_plot(word_counts, title_suffix=None, ax=None,
                    figsize=None):
    title = 'Distribution of Word Counts'
    ax = word_counts.plot(kind='density',
                          title=full_title(title, title_suffix),
                          ax=ax,
                          figsize=figsize)
    ax.set_xlabel('Words per Message')

def word_cloud(messages, width=12, height=12,
               max_font_size=40):
    text = " ".join(chain.from_iterable(filter_stopwords(messages)))
    cloud = WordCloud(max_font_size=max_font_size).generate(text)
    plt.figure(figsize=(width, height))
    plt.imshow(cloud, interpolation='bilinear')
    plt.axis("off")

def comparison_plot(plot_func, from_data, to_data,
                    width=12, height=6):
    if from_data.empty and to_data.empty:
        return

    fig_size = (width, height)
    if from_data.empty:
        plot_func(to_data, title_suffix='To Me', figsize=fig_size)
        return
    if to_data.empty:
        plot_func(from_data, title_suffix='From Me', figsize=fig_size)
        return

    _, ax = plt.subplots(1, 2, figsize=fig_size)
    plot_func(from_data, title_suffix='From Me', ax=ax[0])
    plot_func(to_data, title_suffix='To Me', ax=ax[1])

def summary_table(messages, sentiment, metrics=None):
    if metrics is None:
        metrics = DEFAULT_METRICS

    table = [[metric.name, metric.formatted(messages, sentiment)] \
             for metric in metrics]
    print(tabulate(table, headers=['Metric', 'Value'], tablefmt='orgtbl'))

def emoji_summary(emojis, title_suffix=None):
    emojis = emojis['Emoji'].values.tolist()
    rank = [x+1 for x in range(len(emojis))]
    table = [x for x in zip(rank, emojis)]
    title = 'Emoji Rank'
    headers = [full_title(title, title_suffix), 'Emoji']
    print(tabulate(table, headers=headers))

def summary_comparison(from_messages, from_sentiment,
                       to_messages, to_sentiment,
                       metrics=None):
    if metrics is None:
        metrics = DEFAULT_METRICS

    table = [[metric.name,
              metric.formatted(from_messages, from_sentiment),
              metric.formatted(to_messages, to_sentiment)] \
             for metric in metrics]
    print(tabulate(table, headers=['Metric', 'From Me', 'To Me'],
                   tablefmt='orgtbl'))

def emoji_comparison(from_emojis, to_emojis):
    if from_emojis.empty and to_emojis.empty:
        return
    if from_emojis.empty:
        emoji_summary(to_emojis, title_suffix='To Me')
        return
    if to_emojis.empty:
        emoji_summary(from_emojis, title_suffix='From Me')
        return

    from_emojis = from_emojis['Emoji'].values.tolist()
    to_emojis = to_emojis['Emoji'].values.tolist()
    rank = [x+1 for x in range(len(to_emojis))]
    table = [x for x in zip(rank, from_emojis, to_emojis)]
    print(tabulate(table, headers=['Emoji Rank', 'From Me', 'To Me']))
