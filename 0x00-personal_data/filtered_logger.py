#!/usr/bin/env python3
"""Function filter_datum that return the log messsage
obfuscated
"""
from typing import List
import re

def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Return the log message
    Args:
        fields: list of str representing all field to obfuscate
        redaction: str representing by which field to obfuscated
        message: str representing the log line
        seperator: str representing by character as a seperator
    """
    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
        
    return message
