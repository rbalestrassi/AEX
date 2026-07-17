import http.server
import socketserver
import os
import re

PORT = 3000
DIRECTORY = "/Users/Baletrassi/Documents/AEX-Portfolio"

class RangeHandler(http.server.SimpleHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        pass  # silencia logs

    def do_GET(self):
        path = self.translate_path(self.path)
        range_header = self.headers.get('Range', None)

        if range_header and os.path.isfile(path):
            self._serve_range(path, range_header)
        else:
            super().do_GET()

    def _serve_range(self, path, range_header):
        file_size = os.path.getsize(path)
        m = re.search(r'bytes=(\d*)-(\d*)', range_header)
        if not m:
            self.send_error(400, "Invalid Range")
            return

        start = int(m.group(1)) if m.group(1) else 0
        end   = int(m.group(2)) if m.group(2) else file_size - 1
        end   = min(end, file_size - 1)
        length = end - start + 1

        ctype = self.guess_type(path)
        self.send_response(206)
        self.send_header('Content-Type', ctype)
        self.send_header('Content-Range', f'bytes {start}-{end}/{file_size}')
        self.send_header('Content-Length', str(length))
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Connection', 'close')  # Close after each response to avoid keep-alive issues
        self.end_headers()

        with open(path, 'rb') as f:
            f.seek(start)
            remaining = length
            while remaining > 0:
                chunk = f.read(min(65536, remaining))
                if not chunk:
                    break
                self.wfile.write(chunk)
                remaining -= len(chunk)
        self.wfile.flush()

    def end_headers(self):
        self.send_header('Accept-Ranges', 'bytes')
        super().end_headers()

    def do_HEAD(self):
        """Return full file info for HEAD requests (used by Chrome to probe video)."""
        path = self.translate_path(self.path)
        if os.path.isfile(path):
            file_size = os.path.getsize(path)
            ctype = self.guess_type(path)
            self.send_response(200)
            self.send_header('Content-Type', ctype)
            self.send_header('Content-Length', str(file_size))
            self.send_header('Accept-Ranges', 'bytes')
            self.send_header('Connection', 'close')
            self.end_headers()
        else:
            super().do_HEAD()

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True

with ThreadedTCPServer(("", PORT), RangeHandler) as httpd:
    print(f"Serving AEX Portfolio at http://localhost:{PORT}")
    httpd.serve_forever()
