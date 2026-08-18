# Day 004: Flask Auth & Sliding-Window Rate Limiter Decorators

- **Date:** 2026-08-18
- **Category:** Flask Mini-Features
- **Difficulty:** Intermediate

---

# Flask Auth & Sliding-Window Rate Limiter Decorators

## Background
In microservices and API development, route decorators are used to enforce authentication and rate limiting without bloating route logic.

## Requirements
Implement the decorators in `solution.py`:
1. `require_api_key(valid_keys: set[str])`:
   - Checks `request.headers.get("X-API-Key")` or `Authorization: Bearer <key>`.
   - If missing or invalid, returns `{"error": "Unauthorized", "message": "Invalid or missing API key"}`, status code `401`.
   - If valid, proceeds to execute the decorated route.

2. `RateLimiter(max_requests: int, window_seconds: int)`:
   - Thread-safe in-memory sliding window rate limiter tracking client IP (`request.remote_addr`).
   - If client exceeds `max_requests` within the last `window_seconds`, returns `{"error": "Too Many Requests", "retry_after": <seconds>}`, status code `429`.
   - Otherwise, records request timestamp and allows execution.

## Run Tests
```bash
python test_solution.py
```
