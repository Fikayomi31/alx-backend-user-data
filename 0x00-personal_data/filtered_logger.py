#!/usr/bin/env python3
"""Function filter_datum that return the log messsage
obfuscated
"""
import os
from typing import List
import re
import logging
import mysql.connector


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """intializing the clas
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """doc doc doc
        """
        message = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION,
                            message, self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Return the replace occurrences of certain field values.
    Args:
        fields: list of str representing all field to obfuscate
        redaction: str representing by which field to obfuscated
        message: str representing the log line
        seperator: str representing by character as a seperator
    """
    for field in fields:
        # (.*?) means any character like xxx
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """logging formating
    return logging.Logger
    """
    # Creating a logger name user_data
    logger = logging.getLogger('user_data')
    # Setting the logging level to INFO
    logger.setLevel(logging.INFO)
    # Prevent propagation of log message
    logger.propagate = False
    # Using StramHandle to output the message
    handle = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    handle.setFormatter(formatter)
    logger.addHandler(handle)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    return db connection
    """
    user = os.getenv('PERSONAL_DATA_DB_USERNAME') or "root"
    passwd = os.getenv('PERSONAL_DATA_DB_PASSWORD') or ""
    host = os.getenv('PERSONAL_DATA_DB_HOST') or "localhost"
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')
    conn = mysql.connector.connect(user=user,
                                   password=passwd,
                                   host=host,
                                   database=db_name)
    return conn