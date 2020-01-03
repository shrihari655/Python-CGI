#!C:\Users\srihari\AppData\Local\Programs\Python\Python36-32

print("Content-type:text/html")

print()

import cgi,cgitb,pymysql

cgitb.enable()

form=cgi.FieldStorage()

u=form.getvalue("userName")
p=form.getvalue("pwd")

conn=pymysql.connect(host="localhost",user="root",password="",database="cgi")

cur=conn.cursor()

q1="select * from admin where name='%s' and password='%s'"%(u,p)

cur.execute(q1)

row=cur.rowcount

if row==0:
	print("<center><b><font color='red'>Invalid Credentials!</font></b></center>")
	print("<center><br><a href='index.html'>Login</a></center>")

else:
	#print("<br><center><b><font color='green'>Login Success</font></b></center>")
	print("Login success... redirecting.")
	print("<meta http-equiv='Refresh' content='2;url=adminhome.html'>")








