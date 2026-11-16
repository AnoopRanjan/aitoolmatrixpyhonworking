"""
WSGI Entry Point for Web Hosting & Production Servers
=====================================================
Compatible with:
- Gunicorn (Render, Railway, Heroku, DigitalOcean, Linux VPS)
- Waitress (Windows Server, Azure)
- uWSGI (Nginx, Debian/Ubuntu)
- cPanel Python App Manager / Phusion Passenger
- PythonAnywhere WSGI Configuration
"""

import sys
import os

# Ensure current directory is in Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import application, app

# Expose both standard names
__all__ = ["application", "app"]
