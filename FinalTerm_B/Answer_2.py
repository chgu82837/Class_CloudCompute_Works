#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import call
import os
import platform
import random
import cgi, cgitb

sexOption = [1,2]

locationOption = [
    # [ID,Location_name],
    ['F',"新北市"],
    ['A','臺北市'],
    ['B','臺中市'],
    ['C','基隆市'],
    ['D','臺南市'],
    ['E','高雄市'],
    ['G','宜蘭市'],
    ['H','桃園市'],
    ['I','嘉義市'],
    ['J','新竹縣'],
    ['K','苗栗縣'],
    ['M','南投縣'],
    ['N','彰化縣'],
    ['O','新竹市'],
    ['P','雲林縣'],
    ['Q','嘉義縣'],
    ['T','屏東縣'],
    ['U','花蓮縣'],
    ['V','臺東縣'],
    ['W','金門縣'],
    ['X','澎湖縣'],
    ['Z','連江縣'],
    ['L','臺中縣'],
    ['R','臺南縣'],
    ['S','高雄縣'],
    ['Y','陽明山管理局'],
]

def chk(alpha,sex_val):
    id=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num=[10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 20, 21, 22, 35, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33]
    a2n=dict(zip(id, num))
    # alpha = random.choice(id)
    r = [sex_val]+random.sample(range(0, 10), 7)
    k = [ v*(8-i) for i,v in enumerate(r) ]
    chk = (a2n[alpha]/10)+(a2n[alpha]%10*9) + sum(k)
    chk = (10 - (chk % 10)) % 10
    return alpha+''.join(map(str, r))+str(chk)

def gen_digi():
    return random.randint(0,9)

print "Content-type:text/html\r\n"
print \
"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Question 2</title>
</head>
<body>
<h1>Question 2</h1>
<form action="/Q2.py" method="POST" target="_blank">
	<select name="bir">
"""

for x in locationOption:
	print "<option value=\"%s\">%s</option>" % (x[0],x[1])

print \
"""	</select>
<input type="checkbox" name="male" value="on" /> male
<input type="checkbox" name="female" value="on" /> female
<input type="submit" value="submit" />
</form>
"""

result = ""

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

if form.getvalue('male'):
    sex_val = 1
elif form.getvalue('female'):
	sex_val = 2
else:
    sex_val = sexOption[random.randint(0,len(sexOption) - 1)]

# result += "sex_val = %d " % (sex_val)

# Get data from fields
if form.getvalue('bir'):
	locationChar = form.getvalue('bir')
else:
	locationChar = locationOption[random.randint(0,len(locationOption) - 1)][0]

# result += "locationChar = %s " % (locationChar)

result += "ID generated: %s" % (chk(locationChar,sex_val))

print "<h2>%s</h2>" % (result,)

print \
"""</body>
</html>
"""
