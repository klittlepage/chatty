import os
import sqlite3

from datetime import datetime, timezone

CHAT_DB_PATH = os.path.expanduser('~/Library/Messages/chat.db')


def chat(recipient_id,
         from_me,
         chat_db_path=CHAT_DB_PATH,
         include_timestamps=False):
    def parse_datetime(timestamp):
        timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        return timestamp.astimezone(timezone.utc)

    def entry(row, include_timestamps):
        return (parse_datetime(row[1]), row[0]) if \
            include_timestamps else row[0]

    sql = """
    SELECT
        text,
        datetime(date/1000000000 + 978307200, 'unixepoch') as time
    FROM
        message
    INNER JOIN
        handle
    ON
        message.handle_id = handle.rowid
    WHERE
        handle.id = ?
    AND
        is_from_me = ?
    """
    with sqlite3.connect(f"file:{chat_db_path}?mode=ro", uri=True) as conn:
        cursor = conn.cursor()
        return [entry(message, include_timestamps) for message in
                cursor.execute(sql, (recipient_id, from_me))]
