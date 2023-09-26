import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="root", database="negozio")

cur = myconn.cursor()

try:
    sql = "insert into Dipendente(id, nome, stipendio, id_reparto, ruolo) values (%s, %s, %s, %s, %s)"
    val = [(2, "Giuseppe", 25000, 201, "Dipendente"),
           (3, "Filippo", 25000, 202, "Dipendente"),
           (4, "Marcello", 90000, 201, "Dirigente")]

    cur.executemany(sql,val)
    myconn.commit() #metodo che assicura che le modifiche apportate al db avvengano realmente

except:
    myconn.rollback()

myconn.close()