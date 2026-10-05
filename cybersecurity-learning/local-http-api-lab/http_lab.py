"""Demonstrate two HTTP requests to a JSON API running on this machine."""

import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.error import HTTPError
from urllib.request import ProxyHandler, build_opener


class LabHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/hello":
            status = 200
            payload = {"message": "Hello from the local API", "status": "ok"}
        else:
            status = 404
            payload = {"error": "Resource not found"}
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        # Keep the demonstration output focused on the observed responses.
        pass


def inspect_response(opener, url):
    try:
        response = opener.open(url, timeout=5)
    except HTTPError as error:
        # HTTPError still carries the response status, headers and body.
        response = error
    with response:
        return {
            "path": url.split("/", 3)[-1],
            "status": response.code,
            "content_type": response.headers.get("Content-Type"),
            "nosniff": response.headers.get("X-Content-Type-Options"),
            "body": json.loads(response.read().decode("utf-8")),
        }


def run_demo():
    # Disable proxy use so the loopback requests stay on this machine.
    opener = build_opener(ProxyHandler({}))
    server = HTTPServer(("127.0.0.1", 0), LabHandler)
    worker = threading.Thread(target=server.serve_forever, daemon=True)
    worker.start()
    try:
        origin = "http://127.0.0.1:" + str(server.server_port)
        return [
            inspect_response(opener, origin + "/api/hello"),
            inspect_response(opener, origin + "/api/missing"),
        ]
    finally:
        server.shutdown()
        server.server_close()
        worker.join(timeout=5)


if __name__ == "__main__":
    print(json.dumps(run_demo(), indent=2))
