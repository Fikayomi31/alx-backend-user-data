#!/usr/bin/env python3
"""Defining the class Auth to manage API authentication"""
from flask import Flask, request
from typing import List, TypeVar

class Auth:
    """Representation of the class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns false-path and excluded_paths 
        Args:
            path: path
            excluded_path: excluded path
        return: Flase
        """
        return False
    
    def authorization_header(self, request=None) -> str:
        """Reeturn None
        Args:
            request: None
        """
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """Return None
        Args:
            request: none
        """
        return None
