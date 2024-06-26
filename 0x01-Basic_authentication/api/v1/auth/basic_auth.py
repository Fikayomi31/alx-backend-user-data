#!/usr/bin/env python3
"""Creating a class for BasicAuth"""
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


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

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password."""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
            return None
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return a user instance base on a received request"""
        auth_header = self.authorization_header(request)
        if auth_header is not None:
            token = self.extract_base64_authorization_header(auth_header)
            if token is not None:
                decode = self.decode_base64_authorization_header(token)
                if decode is not None:
                    email, password = self.extract_user_credentials(decode)
                    if email is not None:
                        return self.user_object_from_credentials(email,
                                                                 password)
        return
