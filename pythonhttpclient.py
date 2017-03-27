import pycurl
from io import BytesIO

#PycURL does not provide storage for the network response, so we need a buffer
buffer = BytesIO()

c = pycurl.Curl()
c.setopt(c.VERBOSE, True)
c.setopt(c.URL, 'www.google.com')
c.setopt(c.WRITEDATA,buffer)
c.perform()
c.close()

body = buffer.getvalue()

# Body is a byte string.
# We have to know the encoding in order to print it to a text file
# such as standard output.
print(body.decode('iso-8859-1'))

#http://pycurl.io/docs/latest/quickstart.html
