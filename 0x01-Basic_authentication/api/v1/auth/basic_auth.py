#!/usr/bin/env python3
"""Creating a class for BasicAuth"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Representation of the class"""

    def __init__(self) -> None:
        """doc doc doc"""
        super().__init__()
        
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header
        for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        token = authorization_header.split(' ')[-1]
        return token
