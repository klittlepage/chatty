# Introduction

Curious about the texting habits of you and your friends? Look no further! Chatty will pull texts from iMessage and show you stats on how you communicate with whatever individual you tell it to analyze.

# Why?

Why not? Texting styles are a hot topic of discussion in my friend group. I wanted quantitative evidence that some of my friends are better texters than others. Kidding. Kind of.

# Installation

Out of the box, Chatty will only work on an OSX computer with iMessage. You can relax the iMessage requirement by passing messages from a custom source, as described in the section on [hacking Chatty](#hacking). A working Python 3 [Anaconda](https://anaconda.org/anaconda/python) environment is required. Once Anaconda is installed, run:

```conda env create -f environment.yml```

to install Chatty's dependencies.

# Running

Launch chatty by running:

```
source activate chatty
jupyter notebook
```

Once the notebook loads, redefine ```RECIPIENT_ID``` and reevaluate all cells to see the analysis.

# Hacking

All analysis functions are composable and built for reuse. By default, Chatty will analyze messages sent to/from the counter party defined by ```RECIPIENT_ID```. You can change this behavior by redefining ```from_messages``` and ```to_messages``` before the analysis functions are called.

# Todo

* Support other message sources (WhatsApp/Line/etc)
* Add time series/trend analysis
* PRs welcome

# License

Chatty is released under the [MIT License](https://opensource.org/licenses/MIT).
