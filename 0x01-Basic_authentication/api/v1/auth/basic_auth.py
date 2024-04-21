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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """returns the decoded value of a Base64 string
        base64_authorization_header
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decode_bytes = base64.b64decode(base64_authorization_header)
            return decode_bytes.decode('utf-8')
        except Exception as e:
            return None

    def extract_user_credentials(self,
                                 decode_base64_authorization_header:
                                 str) -> str:
        """Return the user email and password
        from the Base64 decoded value
        """
        if decode_base64_authorization_header is None:
            return None, None
        if not isinstance(decode_base64_authorization_header, str):
            return None, None
        if ':' not in decode_base64_authorization_header:
            return None, None
        email = decode_base64_authorization_header.split(':')[0]
        password = decode_base64_authorization_header.split(':')[1]
        return email, password
