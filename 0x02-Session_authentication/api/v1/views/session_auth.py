#!/usr/bin/env python3
"""Flask view that handles all routes for the
Session authentication
"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ Handle Login
    """
    user_email = request.form.get('email')
    user_password = request.form.get('password')
    if not user_email:
        return jsonify({'error': 'email missing'}), 400
    if not user_password:
        return jsonify({'error': 'password missing'}), 400
    user = User.search({'email': user_email})
    if not user or user = []:
        return jsonify({'error': 'no user found for this email'}), 404
    for u in user:
        if u.is_valid_password(user_password):
            user_id = u.id
            from api.v1.app import auth
            session_id = auth.create_session(user_id)
            response = jsonify(u.to_json())
            response.set_cookie(getenv('SESSION_NAME'), session_id)
            return response
    return jsonify({'error': "wrong password"}), 404


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout():
    """New method that delete user"""
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
