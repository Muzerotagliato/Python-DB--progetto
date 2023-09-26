import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="root", database="negozio") #creo la connessione

cur = myconn.cursor()

try:

    dbs = cur.execute(
        #"alter table Dipendente add data_di_nascita varchar(20) not null" #aggiungo una colonna
        "alter table Dipendente drop data_di_nascita" #rimuovo la colonna
    )
except:
    myconn.rollback()

    myconn.close()