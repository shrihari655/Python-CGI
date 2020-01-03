#!C:\Users\srihari\AppData\Local\Programs\Python\Python37-32

print("Content-type:text/html")

print()

import cgi,cgitb,pymysql

cgitb.enable()

form=cgi.FieldStorage()

u=form.getvalue("userName")
p=form.getvalue("pwd")

conn=pymysql.connect(host="localhost",user="root",password="",database="cgi")

cur=conn.cursor()

q1="select * from students where userName='%s' and password='%s'"%(u,p)

cur.execute(q1)

row=cur.rowcount

if row==0:
	print("<center><b><font color='red'>Invalid Credentials!</font></b></center>")

else:
	print("<br><center><b><font color='green'>Login Success</font></b></center>")








