import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="root", database="negozio")

cur = myconn.cursor()

try:
    sql = "insert into Dipendente(id, nome, stipendio, id_reparto, ruolo) values (%s, %s, %s, %s, %s)"
    val = (1, "Andrea", 25000.00, 201, "Dipendente")

    cur.execute(sql,val)
    myconn.commit() #metodo che assicura che le modifiche apportate al db avvengano realmente

except:
    myconn.rollback()

myconn.close()