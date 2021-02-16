import codecs
import re

from collections import defaultdict
from datetime import datetime


def chat(log_path, include_timestamps=False):
    chat_regex = re.compile(r"(^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{1,2}, "
                            "[0-9]{1,2}:[0-9]" "{1,2}:[0-9]{1,2} (A|P)M): "
                            "(.+?): (.+)")
    chat_parsed = defaultdict(list)
    with codecs.open(log_path, encoding='utf-8') as input_file:
        for line in input_file:
            match = chat_regex.match(line)
            if match:
                message = match.group(4).strip()
                if message == '<‎image omitted>':
                    continue
                if include_timestamps:
                    time = datetime.strptime(match.group(1),
                                             '%m/%d/%y, %H:%M:%S %p')
                    entry = (time, message)
                else:
                    entry = message
                chat_parsed[match.group(3)].append(entry)

    return chat_parsed
