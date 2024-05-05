#!/usr/bin/env python3
"""Creating storage for session id"""
from models.base import Base


class UserSession(Base):
    """Class for usersession"""

    def __init__(self, *args: list, **kwargs: dict):
        """Initialization of usersession"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
        