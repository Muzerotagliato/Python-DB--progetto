import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="root", database="negozio") #creo la connessione

cur = myconn.cursor()

try:

    dbs = cur.execute(
        "create table Dipendente(id int(20) not null primary key, nome varchar(20) not null, stipendio float not null,"
        " ruolo varchar(50), id_reparto int)")

except:
    myconn.rollback()

    myconn.close()