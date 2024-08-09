# models.py

import mysql.connector
from datetime import datetime
from .config import db_config

class ExceptionLogger:
    def __init__(self):
        self.conn = mysql.connector.connect(**db_config)
        self.cursor = self.conn.cursor()

    def log_exception(self, message, stack_trace):
        try:
            query = """
            INSERT INTO ExceptionLog (message, stack_trace, timestamp)
            VALUES (%s, %s, %s)
            """
            timestamp = datetime.utcnow()
            self.cursor.execute(query, (message, stack_trace, timestamp))
            self.conn.commit()
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def __del__(self):
        self.cursor.close()
        self.conn.close()
