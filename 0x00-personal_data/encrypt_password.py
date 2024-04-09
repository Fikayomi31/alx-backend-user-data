#!/usr/bin/env python3
"""function that expects one string argument
name password and returns a salted,
hashed password, which is a byte string
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """doc"""
    pwd = password.encode()
    # Generate a salt and hash a password
    hashed_password = bcrypt.hashpw(pwd, bcrypt.gensalt())
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validate that the provided password 
    matches the hashed password.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)