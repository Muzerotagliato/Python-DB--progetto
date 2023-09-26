import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="root") #creo la connessione

# utilizzo il metodo cursor sull'oggetto connection per creare un oggetto cursor
cur = myconn.cursor()

#tramite il metodo execute vaoo a definire due query

try:
    #query creazione nuovo database
    cur.execute('create database negozio')

    #query per avere la lista dei database
    cur.execute('show databases')

    for x in cur:
        print(x)

except:
    myconn.rollback()
    #il metodo rollback() viene utilizzato per annullare le modifiche apportate al database
    #Utile perchè se si verifica un errore durante le operazioni del database,
    #dopo l'esecuzione di rollback, nessuna modifica apportata alla transazione corrente viene conservata

myconn.close()
#Dobbiamo chiudere la connessione al db dopo aver eseguito tutte le operazioni relative al db