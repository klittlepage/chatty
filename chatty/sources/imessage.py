import os
import sqlite3

CHAT_DB_PATH = os.path.expanduser('~/Library/Messages/chat.db')

def chat(recipient_id, from_me, chat_db_path=CHAT_DB_PATH):
    sql = """
    SELECT
        text
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
        return [message[0] for message in \
                cursor.execute(sql, (recipient_id, from_me))]
