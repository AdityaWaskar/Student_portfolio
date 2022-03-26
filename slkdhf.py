import mysql.connector as sql

mydb = sql.connect(host="localhost", user="root", passwd="", database="SP")
mycursor = mydb.cursor()

passw= "admin"
user= "admin"

sql = "select * from login where username = %s and password = %s"
mycursor.execute(sql, [(user), (passw)])
result = mycursor.fetchall()
if result:
            print("sucess")

# user, passw = mycursor.execute("select username, password from login")

print(result)

def forgot_pass(self):
    self.root.toplevel()