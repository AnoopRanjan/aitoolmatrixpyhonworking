#!/usr/bin/env python3
"""
AI Tools Explorer - Production Python Web Application
======================================================
WSGI-compliant Python web application designed for deployment on any web hosting
provider (Render, Railway, Heroku, Vercel, PythonAnywhere, AWS, Google Cloud, Docker,
or Linux/Windows VPS).

No batch files or desktop launchers required.
Run on hosting:
    gunicorn wsgi:app
or:
    python app.py
"""

import os
import sys
import json
from urllib.parse import parse_qs

# Import data
from tools_data import TOOLS_DATA

# Base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_FILE = os.path.join(BASE_DIR, "index.html")

# Function to read index.html dynamically so changes are reflected immediately
def get_index_content():
    try:
        with open(INDEX_FILE, "rb") as f:
            return f.read()
    except Exception as e:
        return f"<h1>Error loading index.html: {e}</h1>".encode("utf-8")

TOOLS_JSON_BYTES = json.dumps(TOOLS_DATA, indent=2, ensure_ascii=False).encode("utf-8")


def application(environ, start_response):
    """
    Standard WSGI Application Callable.
    Compatible with Gunicorn, uWSGI, Waitress, mod_wsgi, Passenger, AWS Lambda,
    Vercel, and wsgiref.
    """
    path = environ.get("PATH_INFO", "/").rstrip("/")
    method = environ.get("REQUEST_METHOD", "GET")

    # Common CORS headers
    cors_headers = [
        ("Access-Control-Allow-Origin", "*"),
        ("Access-Control-Allow-Methods", "GET, OPTIONS, HEAD"),
        ("Access-Control-Allow-Headers", "Content-Type"),
    ]

    # Handle OPTIONS preflight
    if method == "OPTIONS":
        start_response("200 OK", cors_headers + [("Content-Length", "0")])
        return [b""]

    # Route 1: Home page / Index HTML
    if path in ("", "/index.html", "/home"):
        html_content = get_index_content()
        headers = [
            ("Content-Type", "text/html; charset=utf-8"),
            ("Content-Length", str(len(html_content))),
            ("Cache-Control", "public, max-age=3600"),
        ] + cors_headers
        start_response("200 OK", headers)
        return [html_content]

    # Route 2: REST API - All Tools
    elif path == "/api/tools":
        headers = [
            ("Content-Type", "application/json; charset=utf-8"),
            ("Content-Length", str(len(TOOLS_JSON_BYTES))),
            ("Cache-Control", "public, max-age=600"),
        ] + cors_headers
        start_response("200 OK", headers)
        return [TOOLS_JSON_BYTES]

    # Route 3: REST API - Single Tool by ID (/api/tools/<id>)
    elif path.startswith("/api/tools/"):
        tool_id = path.replace("/api/tools/", "").strip()
        matched = next((t for t in TOOLS_DATA if t["id"].lower() == tool_id.lower()), None)
        if matched:
            body = json.dumps(matched, indent=2, ensure_ascii=False).encode("utf-8")
            headers = [
                ("Content-Type", "application/json; charset=utf-8"),
                ("Content-Length", str(len(body))),
            ] + cors_headers
            start_response("200 OK", headers)
            return [body]
        else:
            err = json.dumps({"error": f"Tool '{tool_id}' not found", "code": 404}).encode("utf-8")
            start_response("404 Not Found", [("Content-Type", "application/json")] + cors_headers)
            return [err]

    # Route 4: Health check endpoint (for Cloud Hosting platforms)
    elif path in ("/health", "/healthz"):
        health_body = json.dumps({
            "status": "healthy",
            "tools_count": len(TOOLS_DATA),
            "platform": sys.platform,
            "version": "1.0.0"
        }).encode("utf-8")
        headers = [
            ("Content-Type", "application/json; charset=utf-8"),
            ("Content-Length", str(len(health_body))),
        ] + cors_headers
        start_response("200 OK", headers)
        return [health_body]

    # Route 5: Static file fallback (e.g. tools.json, favicon, etc.)
    safe_rel_path = path.lstrip("/")
    candidate_file = os.path.join(BASE_DIR, safe_rel_path)
    if os.path.exists(candidate_file) and os.path.isfile(candidate_file):
        try:
            with open(candidate_file, "rb") as cf:
                file_bytes = cf.read()
            mime = "text/plain"
            if candidate_file.endswith(".json"):
                mime = "application/json"
            elif candidate_file.endswith(".html"):
                mime = "text/html"
            elif candidate_file.endswith(".css"):
                mime = "text/css"
            elif candidate_file.endswith(".js"):
                mime = "application/javascript"

            headers = [
                ("Content-Type", mime),
                ("Content-Length", str(len(file_bytes))),
            ] + cors_headers
            start_response("200 OK", headers)
            return [file_bytes]
        except Exception:
            pass

    # Default Fallback: Serve index page (SPA friendly)
    html_fallback = get_index_content()
    start_response("200 OK", [
        ("Content-Type", "text/html; charset=utf-8"),
        ("Content-Length", str(len(html_fallback)))
    ] + cors_headers)
    return [html_fallback]


# Expose standard WSGI aliases for hosting services
app = application


def main():
    """
    Built-in standalone server runner when executing `python app.py`.
    Listens on 0.0.0.0 and dynamically checks the PORT environment variable.
    """
    from wsgiref.simple_server import make_server

    # Cloud hosting providers (Render, Heroku, Railway, Cloud Run, AWS) pass PORT env var
    port_str = os.environ.get("PORT", "5000")
    try:
        port = int(port_str)
    except ValueError:
        port = 5000

    host = os.environ.get("HOST", "0.0.0.0")

    print("=" * 70)
    print(" 🌐 AI TOOLS WEBSITE - PRODUCTION WEB SERVER")
    print("=" * 70)
    print(f" Environment : Hosting / Cloud Ready")
    print(f" Listening on: http://{host}:{port}")
    print(f" Tools count : {len(TOOLS_DATA)}")
    print(f" WSGI Object : app / application")
    print("=" * 70)

    try:
        with make_server(host, port, application) as httpd:
            print(f"[+] Serving on http://{host}:{port} ... (Press Ctrl+C to stop)")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Server stopped.")


if __name__ == "__main__":
    main()
