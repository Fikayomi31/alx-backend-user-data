#!/usr/bin/env python3
"""Flask view that handles all routes for the
Session authentication
"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ Handle Login
    """
    user_email = request.form.get('email')
    user_pwd = request.form.get('password')
    if user_email is None or user_email == '':
        return jsonify({"error": "email missing"}), 400
    if user_pwd is None or user_pwd == '':
        return jsonify({"error": "password missing"}), 400
    users = User.search({"email": user_email})
    if not users or users == []:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if user.is_valid_password(user_pwd):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            response = jsonify(user.to_json())
            session_name = os.getenv('SESSION_NAME')
            response.set_cookie(session_name, session_id)
            return response
    return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout():
    """New method that delete user"""
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
