#!C:\Users\srihari\AppData\Local\Programs\Python\Python36-32

print("Content-type:text/html")

print()

import cgi,cgitb,pymysql

form=cgi.FieldStorage()

item=form.getvalue('item')

conn=pymysql.connect(host="localhost",user="root",password="",database="cgi")

cur=conn.cursor()

q1="select * from admin where id='%s' or userName='%s'"%(item,item)

cur.execute(q1)

row=cur.rowcount

if row==0:
	print("<center><b><font color='red'>No records Exist!</font></b></center>")
	

else:
	
	rec=cur.fetchall()
	
	print("<center><h1>Records</h1>")
	
	print("<table style='width:800px;border:solid grey 2px;font-size:20px;text-align:center;background-color:lightgreen'>")
	
	print("<tr style='background-color:black;color:white;font-size:20px;'><th>Id</th><th>Name</th><th>Password</th><th>Gender</th><th>Languages</th><th>State</th></tr>")
	
	for col in rec:
		
		print("<tr>")
		print("<td>",col[0],"</td>")
		print("<td>",col[1],"</td>")
		print("<td>",col[2],"</td>")
		print("<td>",col[3],"</td>")
		print("<td>",col[4],"</td>")
		print("<td>",col[5],"</td>")
		print("</tr>")

	print("</table>")
		
	
print("<center><h3><a href='adminhome.html'>Back</a></h3>")






