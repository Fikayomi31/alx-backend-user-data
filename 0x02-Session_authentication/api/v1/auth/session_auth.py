#!/usr/bin/env python3
"""Create a class SessionAuth that inherits from Auth
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """an instance method that returns a User ID
        based on a Session ID
        Args:
            session_id - session_id for the user
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
    
    def current_user(self, request=None):
        """ Method to return user instance based
        on a cookie value"""
        if request:
            session_cookie = self.session_cookie(request)
            user_id = self.user_id_by_session_id(session_cookie)
            return  User.get(user_id)
