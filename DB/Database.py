import mysql.connector
#creating connection object
mydb = mysql.connector.connect(host="brainographydb.cse1mvnkc219.us-west-2.rds.amazonaws.com",user="braino",passwd = "brainography", database = "brainodb")

mycursor = mydb.cursor()

mycursor.execute("select * from check_tab")

result = mycursor.fetchall() #fetchone() will give out single record

for i in result:
    print(i)
    
query = "insert into check_tab (name, contact) values(%s, %s)" # %s is common for all data types
d1 = ("Sarang", "123")
d2 = ("Kumar", "456")
mycursor.execute(query, d1)    
mycursor.execute(query, d2)
mydb.commit()   

uq = "update check_tab set name = %s where contact = %s"
u1 = ("tak", "123")
mycursor.execute(uq,u1)
mydb.commit()
 
mydb.close()    
    