# Introduction

Curious about the texting habits of you and your friends? Look no further! Chatty will pull texts from iMessage and show you stats on how you communicate with whatever individual you tell it to analyze.

# Why?

Why not? Texting styles are a hot topic of discussion in my friend group. I wanted quantitative evidence that some of my friends are better texters than others. Kidding. Kind of.

# Installation

A working Python 3 [Anaconda](https://anaconda.org/anaconda/python) environment is required. Once Anaconda is installed, run:

```conda env create -f environment.yml```

to install Chatty's dependencies.

# Running

Launch chatty by running:

```
source activate chatty
jupyter notebook
```

Select a source per the instructions below, and re-evaluate all cells.

## External Variables

Chatty includes a utility for reading config from an external yaml file: ```chatty.load_vars(vars_file='vars.yml')```. Use this method for situations where you wish to share your notebook without exposing sensitive variables (e.g. names or telephone numbers).

## Sources

### iMessage

The iMessage source requires an OSX computer with iMessage. Once the notebook loads, redefine ```RECIPIENT_ID``` to either an E.164 number of the form '+13031234567' or an iMessage handle of the form 'foo@bar.com'.

### Line

The line source reads from a Line chat log exported by the iOS Line client. It has not been tested against other clients.

```python
from chatty.sources import line_chat

project_vars = load_vars()
all_messages = line_chat(project_vars['chat_path'])
from_messages = all_messages[project_vars['from']]
to_messages = all_messages[project_vars['to']]
```

# Hacking

All analysis functions are composable and built for reuse. By default, Chatty will analyze messages sent to/from the counter party defined by ```RECIPIENT_ID```. You can change this behavior by redefining ```from_messages``` and ```to_messages``` before the analysis functions are called.

# Todo

* Support other message sources (WhatsApp/Line/etc)
* Add time series/trend analysis
* PRs welcome

# License

Chatty is released under the [MIT License](https://opensource.org/licenses/MIT).
