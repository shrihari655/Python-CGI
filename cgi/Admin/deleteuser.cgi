#!C:\Users\srihari\AppData\Local\Programs\Python\Python36-32

print("Content-type:text/html")

print()

import cgi,cgitb,pymysql

form=cgi.FieldStorage()

item=form.getvalue('item')

conn=pymysql.connect(host="localhost",user="root",password="",database="cgi")

cur=conn.cursor()

q1="delete from admin where id='%s' or userName='%s'"%(item,item)

cur.execute(q1)

row=cur.rowcount

if row==0:
	print("<center><b><font color='red'>No records Exist to delete!</font></b></center>")
	

else:
	print("<h3>User Deleted... Wait.</h3>")
	print("<meta http-equiv='Refresh' content='2;url=view.cgi'>")

	
print("<center><h3><a href='adminhome.html'>Back</a></h3>")






