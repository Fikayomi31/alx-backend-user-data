#!/usr/bin/env python3
"""Create a class SessionAuth that inherits from Auth
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Creation of class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """An instance that create session
        Arg:
            user_id - session id in str
        Return: the str
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        """Generate a Session ID using uuid module"""
        session_id = str(uuid.uuid4())
        """Session ID as key of the dictionary"""
        self.user_id_by_session_id[session_id] = user_id
        return session_id
