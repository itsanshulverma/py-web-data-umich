'''
Exploring the HyperText Transport Protocol

You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.
    http://data.pr4e.org/intro-short.txt
There are three ways that you might retrieve this web page and look at the response headers:
    Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data. Make sure to change the code to retrieve the above URL - the values are different for each URL.
    Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
Enter the header values in each of the fields below and press "Submit".

'''

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

'''
# Output

HTTP/1.1 200 OK
Date: Mon, 19 Oct 2020 21:07:40 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "1d3-54f6609240717"
Accept-Ranges: bytes
Content-Length: 467
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain

Why should you learn to write programs?

Writing programs (or programming) is a very creative
and rewarding activity.  You can write programs for
many reasons, ranging from making your living to solving
a difficult data analysis problem to having fun to helping
someone else solve a problem.  This book assumes that
everyone needs to know how to program, and that once
you know how to program you will figure out what you want
to do with your newfound skills.
'''

'''
# From Browser Developer Tools:

Request URL: http://data.pr4e.org/intro-short.txt
Request Method: GET
Status Code: 200 OK
Remote Address: 192.241.136.170:80
Referrer Policy: strict-origin-when-cross-origin
Accept-Ranges: bytes
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Connection: Keep-Alive
Content-Length: 467
Content-Type: text/plain
Date: Mon, 19 Oct 2020 20:55:41 GMT
ETag: "1d3-54f6609240717"
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Keep-Alive: timeout=5, max=100
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
Pragma: no-cache
Server: Apache/2.4.18 (Ubuntu)
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Host: data.pr4e.org
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Safari/537.36
'''