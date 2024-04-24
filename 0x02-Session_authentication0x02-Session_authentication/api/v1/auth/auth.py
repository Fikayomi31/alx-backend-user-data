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
        return: False
        """
        if path is None or excluded_paths is None:
            return True
        if len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            path += "/"
        if path in excluded_paths:
            return False
        for excluded_path in excluded_paths:
            if excluded_path.startswith(path):
                return False
            elif path.startswith(excluded_path):
                return False
            elif excluded_path[-1] == "*":
                if path.startswith(excluded_path[:-1]):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Reeturn None
        Args:
            request: None
        """
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Return None
        Args:
            request: none
        """
        return None
