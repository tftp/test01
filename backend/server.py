# main.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Обрабатывает GET-запросы."""
        self.send_response(200)  # Код 200 OK
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b"Hello from Effective Mobile!") # Отправляем байтовое представление строки

def run_server(port=8080):
    """Запускает HTTP-сервер на указанном порту."""
    server_address = ('', port) # Пустая строка означает "слушать на всех доступных интерфейсах"
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Сервер запущен на порту {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
        httpd.server_close()
        sys.exit(0)

if __name__ == "__main__":
    server_port = 8080
    run_server(server_port)
