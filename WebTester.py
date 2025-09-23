# given a url, this python app needs to know if the web server supports http2
#first i want to get the link from the stdIO for when a user does python WebTester.py <someLink>
import re
import sys
#test to see if we get link correctly
#print("the link that was typed was:", sys.argv[1:])
link = sys.argv[1:]
#print(link)
import socket
address =(link[0], 8080)
info = socket.getaddrinfo(link[0], 8080, family=socket.AF_UNSPEC, type=0, proto=0, flags=0)
print(info)
import http.client 
connection = http.client.HTTPSConnection(link[0])
connection.connect()
connection.request("GET", "/")
x = connection.getresponse()
print(x.status)

print(x.reason)
print(x.info)
print(x.getheaders)
print(x.geturl)








# the cookie name, the expire time, and the domain name, of cookkthat th eweb server will use

# also whether or not the requested web page is password-protected
