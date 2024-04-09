#!/usr/bin/env python3
"""function that expects one string argument
name password and returns a salted,
hashed password, which is a byte string
"""
import bcrypt


def hash_password(password):
    """doc"""
    pwd = b"{password}" # password to be treated as bytes literal
    # Generate a salt and hash a password
    hashed_password = bcrypt.hashpw(pwd, bcrypt.gensalt())
    return hashed_password