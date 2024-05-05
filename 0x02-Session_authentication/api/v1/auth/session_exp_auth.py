#!/usr/bin/env python3
"""Session authentication with expiration module for the API.
"""
import os
from flask import request
from datetime import datetime, timedelta
from .session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """Session authentication class with expiration.
    """

    def __init__(self) -> None:
        """Initializes a new SessionExpAuth instance.
        """
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0
        super().__init__()

    def create_session(self, user_id=None):
        """Creates a session id for the user.
        """
        session_id = super().create_session(user_id)
        if type(session_id) != str:
            return None
        data = {
            'user_id': user_id,
            'created_at': datetime.now(),
        }
        self.user_id_by_session_id[session_id] = data
        return session_id

    def user_id_for_session_id(self, session_id=None) -> str:
        """Retrieves the user id of the user associated with
        a given session id.
        """
        if not session_id:
            return None
        data = self.user_id_by_session_id.get(session_id)
        if not data:
            return None
        if self.session_duration <= 0:
            return data.get('user_id')
        if 'created_at' not in data:
            return None
        current_time = datetime.now()
        expiry = data['created_at'] + timedelta(seconds=self.session_duration)
        if expiry < current_time:
            return None
        return data.get('user_id')
