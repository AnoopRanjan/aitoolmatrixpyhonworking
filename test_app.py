"""
Unit & Integration Tests for AI Tools Explorer Website
======================================================
Tests the WSGI application, routing, REST API, data consistency, and hosting readiness.
"""

import sys
import os

# Ensure current directory is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import unittest
import json
import urllib.request
import threading
import time
from wsgiref.simple_server import make_server

from tools_data import TOOLS_DATA
from app import application, app


class TestAIToolsData(unittest.TestCase):
    """Test data consistency and completeness for all 9 tools."""

    def test_total_tools_count(self):
        self.assertEqual(len(TOOLS_DATA), 9, "Must contain exactly 9 AI tools")

    def test_required_tool_ids(self):
        expected_ids = {
            "notebooklm",
            "stitch",
            "aistudio",
            "wisprflow",
            "claude",
            "julius",
            "higgsfield",
            "claude-skills",
            "elevenlabs"
        }
        actual_ids = {t["id"] for t in TOOLS_DATA}
        self.assertEqual(expected_ids, actual_ids, "All 9 expected tool IDs must exist")

    def test_tool_fields(self):
        required_fields = [
            "id", "name", "url", "category", "tagline",
            "youtube_id", "youtube_title", "description",
            "key_features", "how_it_helps", "pricing", "developer"
        ]
        for tool in TOOLS_DATA:
            for field in required_fields:
                self.assertIn(field, tool, f"Tool '{tool.get('id')}' missing required field: {field}")
                self.assertTrue(tool[field], f"Field '{field}' in '{tool['id']}' must not be empty")

    def test_youtube_ids_format(self):
        for tool in TOOLS_DATA:
            yid = tool["youtube_id"]
            self.assertEqual(len(yid), 11, f"YouTube ID for '{tool['id']}' should be 11 characters: {yid}")

    def test_description_is_one_paragraph(self):
        for tool in TOOLS_DATA:
            desc = tool["description"].strip()
            self.assertGreater(len(desc), 200, f"Description for '{tool['id']}' too short")
            self.assertNotIn("\n\n", desc, f"Description for '{tool['id']}' contains multiple paragraphs")


class TestWSGIApplicationHosting(unittest.TestCase):
    """Test WSGI Application endpoints and responses using standard wsgiref server."""

    @classmethod
    def setUpClass(cls):
        cls.port = 5928
        cls.server = make_server("127.0.0.1", cls.port, application)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        time.sleep(0.3)

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def test_home_page_returns_html(self):
        url = f"http://127.0.0.1:{self.port}/"
        with urllib.request.urlopen(url) as resp:
            self.assertEqual(resp.status, 200)
            content = resp.read().decode("utf-8")
            self.assertIn("AI Power Tools Directory", content)
            self.assertIn("NotebookLM", content)

    def test_api_tools_returns_json(self):
        url = f"http://127.0.0.1:{self.port}/api/tools"
        with urllib.request.urlopen(url) as resp:
            self.assertEqual(resp.status, 200)
            self.assertIn("application/json", resp.headers.get("Content-Type"))
            data = json.loads(resp.read().decode("utf-8"))
            self.assertEqual(len(data), 9)

    def test_api_single_tool(self):
        url = f"http://127.0.0.1:{self.port}/api/tools/notebooklm"
        with urllib.request.urlopen(url) as resp:
            self.assertEqual(resp.status, 200)
            data = json.loads(resp.read().decode("utf-8"))
            self.assertEqual(data["id"], "notebooklm")
            self.assertEqual(data["name"], "Google NotebookLM")

    def test_health_endpoint(self):
        url = f"http://127.0.0.1:{self.port}/health"
        with urllib.request.urlopen(url) as resp:
            self.assertEqual(resp.status, 200)
            data = json.loads(resp.read().decode("utf-8"))
            self.assertEqual(data["status"], "healthy")
            self.assertEqual(data["tools_count"], 9)

    def test_wsgi_aliases(self):
        self.assertIs(application, app)


class TestHostingConfigFiles(unittest.TestCase):
    """Verify that all hosting configuration files exist and are populated."""

    def test_hosting_files_exist(self):
        base_dir = os.path.dirname(__file__)
        files = ["wsgi.py", "Procfile", "requirements.txt", "runtime.txt", "render.yaml", "vercel.json", "Dockerfile"]
        for filename in files:
            filepath = os.path.join(base_dir, filename)
            self.assertTrue(os.path.exists(filepath), f"Missing hosting file: {filename}")
            self.assertGreater(os.path.getsize(filepath), 0, f"Empty hosting file: {filename}")


if __name__ == "__main__":
    unittest.main()
