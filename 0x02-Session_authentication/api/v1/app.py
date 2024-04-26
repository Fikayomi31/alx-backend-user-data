#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request, abort
from flask_cors import CORS, cross_origin
import os
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.session_auth import SessionAuth
from api.v1.auth.session_exp_auth import SessionExpAuth

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


auth = None
auth = os.getenv('AUTH_TYPE')
if auth == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth == 'session_auth':
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()
elif auth == 'session_exp_auth':
    from api.v1.auth.session_exp_auth import SessionExpAuth
    auth = SessionExpAuth()
elif auth:
    from api.v1.auth.auth import Auth
    auth = Auth()

@app.before_request
def before_request_func():
    """doc doc doc"""
    if auth is None:
        pass
    else:
        """Setting current_user on request to return
        auto_current_user"""
        if not auth:
        return
    if not auth.require_auth(request.path, [
                             '/api/v1/status/',
                             '/api/v1/unauthorized/',
                             '/api/v1/forbidden/',
                             '/api/v1/auth_session/login/'
                             ]):
        return
    if not (auth.authorization_header(request) or
            auth.session_cookie(request)):
        abort(401)
    iuser = auth.current_user(request)
    if not iuser:
        abort(403)
    request.current_user = iuser


@app.errorhandler(401)
def unauthorized(error) -> str:
    """doc doc Unauthorized handler"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error):
    """Error handler for 403 Forbidden"""
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error) -> str:
    """Not found handler"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
