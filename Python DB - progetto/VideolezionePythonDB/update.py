import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="root", database="negozio")

cur = myconn.cursor()

try:
    cur.execute("update Dipendente set nome = 'Alex' where id=1")
    myconn.commit() #metodo che assicura che le modifiche apportate al db avvengano realmente
    print("UPDATE DONE")

except:
    print("Error")
    myconn.rollback()

myconn.close()