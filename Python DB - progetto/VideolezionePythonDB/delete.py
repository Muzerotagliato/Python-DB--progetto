import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="root", database="negozio")

cur = myconn.cursor()

try:
    cur.execute("delete from Dipendente where id = 1")
    myconn.commit() #metodo che assicura che le modifiche apportate al db avvengano realmente

except:
    myconn.rollback()

myconn.close()