import http.server
import socketserver
import subprocess
import socket

# Function to run an external program
def run_external_program(command):
    try:
        # Run the command
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Optionally, wait for the process to complete and get the output
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            print(f"Program output: {stdout.decode()}")
        else:
            print(f"Error: {stderr.decode()}")
    except Exception as e:
        print(f"Failed to run the program: {e}")

# Handler to serve the HTML content
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Write content
        self.wfile.write(bytes("<html><head><title>My Name</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><h1>Hello, kashif my name is sumair</h1></body></html>", "utf-8"))
        return

# Function to start the HTTP server
def start_http_server(host, port):
    handler_object = MyHttpRequestHandler
    with socketserver.TCPServer((host, port), handler_object) as httpd:
        print(f"Serving HTTP on {host}:{port}")
        httpd.serve_forever()

if __name__ == "__main__":
    # Example command to run
    command = "echo Hello, World!"

    # Run the external program
    run_external_program(command)

    # Start the HTTP server
    HOST = '127.0.0.1'  # Localhost
    PORT =5698         # Port to listen on
    start_http_server(HOST, PORT)

