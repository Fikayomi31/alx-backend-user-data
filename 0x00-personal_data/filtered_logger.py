#!/usr/bin/env python3
"""Function filter_datum that return the log messsage
obfuscated
"""
from typing import List
import re
import logging


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
        redacted = filter_datum(self.fields, self.REDACTION,
                                message, self.SEPARATOR)
        return redacted


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
