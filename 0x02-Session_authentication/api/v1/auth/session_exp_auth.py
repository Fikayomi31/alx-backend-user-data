#!/usr/bin/env python3
""" A class that inherits from SessionAuth """
from api.v1.auth.session_auth import SessionAuth
import os
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """Creation of the class"""

    def __init__(self):
        """Initialization of the class"""
        super().__init__()
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION'))
        except (TypeError, ValueError):
            self.session_duration = 0

    def create_session(self, user_id: str = None):
        """Create a Session ID by calling super()"""
        session_dict = super().create_session(user_id)
        if not session_dict:
            return None
        data = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        self.user_id_by_session_id[session_dict] = data
        return session_dict
    
    def user_id_for_session_id(self, session_id=None):
        """ Overload function"""
        if session_id is None:
            return None
        session = self.user_id_by_session_id.get(session_id)
        if not session:
            return None
        if self.session_duration <= 0:
            return session.get('user_id')
        if 'created_at' not in session:
            return None
        """Calculate expiration time"""
        created_at = session['created_at']
        expiration_time = created_at + timedelta(seconds=self.session_duration)
        if datetime.now() > expiration_time:
            return None
        return session.get('user_id')
        
        