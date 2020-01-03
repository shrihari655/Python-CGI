#!C:\Users\srihari\AppData\Local\Programs\Python\Python37-32\python

print("Content-type:text/html")
print()

import cgi,cgitb,pymysql

cgitb.enable()

form=cgi.FieldStorage()

u=form.getvalue("user")
p=form.getvalue("pwd")
g=form.getvalue("gen")
lanlist=form.getvalue("lan")
c=form.getvalue("city")
q=form.getvalue("qual")
A=form.getvalue("addr")


op=""

for x in lanlist:
	op=op+x+", "


conn=pymysql.connect(host="localhost",user="root",password="",database="cgi")

cur=conn.cursor()

q1="select * from students where userName='%s'"%u

cur.execute(q1)

row=cur.rowcount

if row==0:
	q2="insert into students(userName,password,gender,language,city,qualification,Address) values('%s','%s','%s','%s','%s','%s','%s')"%(u,p,g,op,c,q,A)
	
	cur.execute(q2)	
	
	row2=cur.rowcount
	
	if row2>0:
		print("<center><b><font color='green'>Signup success.</font></b></center>")
	
else:
	print("<center><b><font color='red'>Record with given username already exists</font></b></center>")


print("<br><center><b><font color='rblue'><a href='index.html'>Go Back</a></font></b></center>")







