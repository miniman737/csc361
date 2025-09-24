# given a url, this python app needs to know if the web server supports http2
#first i want to get the link from the stdIO for when a user does python WebTester.py <someLink>
import sys
#test to see if we get link correctly
#print("the link that was typed was:", sys.argv[1:])
argument = sys.argv[1:]
link = argument[0]
print(link)

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((link, 80))
s.send(b"GET /index.html HTTP/1.0\r\n\n\n")

response = s.recv(10000)
s.close()
print(response.decode("utf8"))


import ssl
context = ssl.create_default_context()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn = context.wrap_socket(sock, server_hostname=link)
conn.connect((link, 443))

request = "GET /index.html HTTP/1.0\r\n\n\n"
conn.sendall(request.encode())


response = conn.recv(10000)
conn.close()
print(response.decode())


#HTTP2 support from tutorial
print("HTTP2 test")
context = ssl.create_default_context()
context.set_alpn_protocols(['http/1.1', 'h2'])
with socket.create_connection(("www.google.ca", 443)) as raw:
    with context.wrap_socket(raw, server_hostname="google.ca") as conn:
        proto = conn.selected_alpn_protocol()
        print("Negotiated protocol: {}".format(proto))
#password prottectd
HOST = "httpbin.org"
request = (
    "GET /basic-auth/user/passwd HTTP/1.1\r\n"
    "Host: httpbin.org\r\n"
    "Connection: close\r\n"
    "\r\n"
)

with socket.create_connection((HOST, 80)) as sock:
    sock.sendall(request.encode())
    response = sock.recv(10000)
    print(response.decode())

# the cookie name, the expire time, and the domain name, of cookkthat th eweb server will use

# also whether or not the requested web page is password-protected
