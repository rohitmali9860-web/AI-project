import unittest
from flask import Flask, jsonify
from solution import require_api_key, RateLimiter


class TestFlaskDecorators(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config["TESTING"] = True
        self.valid_keys = {"secret-token-123", "prod-key-xyz"}

        @self.app.route("/secure-data")
        @require_api_key(self.valid_keys)
        def secure_data():
            return jsonify({"status": "success", "data": [1, 2, 3]}), 200

        limiter = RateLimiter(max_requests=2, window_seconds=10)

        @self.app.route("/limited-ping")
        @limiter
        def limited_ping():
            return jsonify({"pong": True}), 200

        self.client = self.app.test_client()

    def test_api_key_header_success(self):
        resp = self.client.get("/secure-data", headers={"X-API-Key": "secret-token-123"})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json["status"], "success")

    def test_bearer_token_success(self):
        resp = self.client.get("/secure-data", headers={"Authorization": "Bearer prod-key-xyz"})
        self.assertEqual(resp.status_code, 200)

    def test_unauthorized_missing_and_wrong_key(self):
        resp1 = self.client.get("/secure-data")
        self.assertEqual(resp1.status_code, 401)
        resp2 = self.client.get("/secure-data", headers={"X-API-Key": "invalid-token"})
        self.assertEqual(resp2.status_code, 401)

    def test_rate_limiter_throttles(self):
        # 1st request -> OK
        r1 = self.client.get("/limited-ping")
        self.assertEqual(r1.status_code, 200)
        # 2nd request -> OK
        r2 = self.client.get("/limited-ping")
        self.assertEqual(r2.status_code, 200)
        # 3rd request -> 429 Too Many Requests
        r3 = self.client.get("/limited-ping")
        self.assertEqual(r3.status_code, 429)


if __name__ == "__main__":
    unittest.main()
