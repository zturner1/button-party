#!/usr/bin/env python3
"""
Simple HTTP server for Telegram Web App development.
Serves static files with CORS headers required by Telegram WebApps.

Note: Telegram WebApps require HTTPS in production.
Use ngrok or Cloudflare Tunnel for local development.
"""

import http.server
import socketserver
import os
from pathlib import Path

PORT = 8080

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP request handler with CORS headers for Telegram WebApps."""
    
    def end_headers(self):
        # Add CORS headers required by Telegram WebApps
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        super().end_headers()
    
    def do_OPTIONS(self):
        # Handle preflight requests
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        # Custom logging with color
        print(f'[SERVER] {self.address_string()} - {format % args}')

def run_server():
    """Start the HTTP server."""
    handler = CORSRequestHandler
    
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"=" * 50)
        print(f"🚀 Telegram Web App Server running on http://localhost:{PORT}")
        print(f"📁 Serving files from: {os.getcwd()}")
        print(f"=" * 50)
        print()
        print("⚠️  IMPORTANT: Telegram requires HTTPS for WebApps!")
        print("   Use ngrok for local development:")
        print(f"   ngrok http {PORT}")
        print()
        print("Press Ctrl+C to stop")
        print("=" * 50)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped")

if __name__ == "__main__":
    run_server()
