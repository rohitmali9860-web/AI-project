"""
Day Challenge: Flask Auth & Sliding-Window Rate Limiter Decorators
"""
from collections import defaultdict, deque
from functools import wraps
import time
from typing import Callable, Set
from flask import Flask, jsonify, request


def require_api_key(valid_keys: Set[str]) -> Callable:
    """
    Decorator that checks request headers for a valid API Key.
    
    Accepts:
    - Header: 'X-API-Key': '<key>'
    - Header: 'Authorization': 'Bearer <key>'
    
    Returns 401 JSON response if key is missing or invalid.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: Extract key from X-API-Key header or Authorization: Bearer <key>
            # TODO: Check if key in valid_keys
            # TODO: If not valid, return jsonify({"error": "Unauthorized", "message": "Invalid or missing API key"}), 401
            # TODO: Otherwise call and return func(*args, **kwargs)
            raise NotImplementedError("TODO: Implement require_api_key wrapper")
        return wrapper
    return decorator


class RateLimiter:
    """Sliding-window rate limiter decorator tracking client IP."""

    def __init__(self, max_requests: int = 5, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.client_records = defaultdict(deque)

    def __call__(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: Get client IP from request.remote_addr or fallback "127.0.0.1"
            # TODO: Clean up timestamps older than (current_time - window_seconds)
            # TODO: If len(records) >= max_requests, return jsonify({"error": "Too Many Requests"}), 429
            # TODO: Append current_time and call func(*args, **kwargs)
            raise NotImplementedError("TODO: Implement RateLimiter wrapper")
        return wrapper
