import csv
import codecs

from collections import defaultdict
from datetime import datetime

def chat(log_path, include_timestamps=False):
    chat_parsed = defaultdict(list)
    with codecs.open(log_path, encoding='utf-8') as input_file:
        input_file.readline()
        input_file.readline()
        reader = csv.reader(input_file, delimiter='\t')
        awaiting_date = True
        for row in reader:
            if not row:
                awaiting_date = True
                continue
            if awaiting_date:
                date_part = row[0]
                awaiting_date = False
                continue
            if len(row) < 3:
                continue
            time, participant = row[:2]
            message = '\t'.join(row[2:])
            if message == '[Photo]' or message == '[Sticker]':
                continue
            if include_timestamps:
                time = datetime.strptime(f"{date_part} {time}",
                                         '%a, %m/%d/%Y %H:%M %p')
                chat_entry = (time, message)
            else:
                chat_entry = message
            chat_parsed[participant].append(chat_entry)

    return chat_parsed
