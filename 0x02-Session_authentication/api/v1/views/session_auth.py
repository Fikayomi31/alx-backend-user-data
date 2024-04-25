#!/usr/bin/env python3
"""Flask view that handles all routes for the
Session authentication
"""
from flask import Flask, request
from api.v1.auth.session_auth import SesssionAuth


