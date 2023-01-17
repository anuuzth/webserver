# python web server  
from http.server import BaseHTTPRequestHandler, HTTPServer
import pandas as pd
from test import format_table
hostName = "localhost"
serverPort = 8080

def prnt():
        df1 = pd.read_csv('data.csv')
        return df1.to_html()

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Data: %s</p>" % format_table() , "utf-8")) #replace'format_table' with 'prnt()' to display using pandas
        self.wfile.write(bytes("<body>", "utf-8")) 
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
     
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")


