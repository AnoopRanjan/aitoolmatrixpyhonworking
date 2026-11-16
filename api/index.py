"""
Vercel Serverless Function Handler
===================================
Enables direct deployment on Vercel without a server.
"""

import sys
import os

# Add parent directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import application as app

# Vercel looks for 'app' or 'handler'
handler = app
