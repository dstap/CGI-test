#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

#Get Form
form = cgi.FieldStorage()

#Get Example Variable A
A = form.getvalue('A')

#HTML Header
print('Content-type: text/html\n\r\n')

#Page or Content
print('<html>')
print('<p>test</p>')

if A == None:
    print("<b>There is No A Value</b>")
else:
    print("<b>The A Value is: " + A + "</b>")


print("<script> A = 1;</script>")
print('</html>')

