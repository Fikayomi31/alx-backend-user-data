#!/usr/bin/env python3
"""Create a new authentication class SessionDBAuth"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """db session authentication"""
    
    def create_session(self, user_id=None):
        """Crete and store new instance of UserSession"""
        if not user_id:
            return None
        session_id = super().create_session(user_id)
        session = UserSession(user_id=user_id, session_id=session_id)
        session.save()
        return session_id
    
    def user_id_for_session_id(self, session_id=None):
        """Returns the User ID by requesting UserSession in the
        database based on session_id"""
        if not session_id:
            return None
        session = UserSession().search(
            {'session_id': session_id})
        if not session:
            return None
        return session[0].user_id
    
    def destroy_session(self, request=None):
        """destroys the UserSession based on the Session
        ID from the request cookie"""
        if not request:
            return False
        session = self.session_cookie(request)
        if not session:
            return False
        curr = UserSession().search({
            "session_id": session
        })
        if not curr or curr == []:
            return False
        curr[0].remove()
        return True
