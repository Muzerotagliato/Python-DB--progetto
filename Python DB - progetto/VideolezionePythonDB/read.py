import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="root", database="negozio")

cur = myconn.cursor(buffered=True)
# In questo caso andremo a utilizzare il cursor con il parametro 'buffered' settato a 'True': Il motivo è che senza un cursore bufferizzato,
# i risultati vengono caricati in modo "pigro", il che significa che un metodo che prenderà solamente il primo risultato di una lista
# di elementi come "fetchone" in realtà recupera solo una riga dall'intero set di risultati della query e quindi quando si utilizzerà
# nuovamente lo stesso cursore, verrà lanciato l'errrore del fatto che ci sono ancora n-1 risultati (dove n è la quantità di risultati)
# in attesa di essere recuperati. Tuttavia, quando si utilizza un cursore bufferizzato, il connettore libererà i record inutilizzati.

try:

    print("Esempio 1: Select di tutta la tabella Dipendente")
    cur.execute("select * from Dipendente")
    result = cur.fetchall()
    for x in result:
        print(x)

    print("")
    print("Esempio 2: Select di alcune colonne della tabella Dipendente")
    cur.execute("select id, nome, stipendio from Dipendente")
    result = cur.fetchall()
    for x in result:
        print(x)

    print("")
    print("Esempio 3: Select del primo elemento della lista di alcune colonne della tabella Dipendente")
    cur.execute("select id, nome, stipendio from Dipendente")
    result = cur.fetchone()
    print(result)

    print("")
    print("Esempio 4: prendere i dati dal risultato della query")
    cur.execute("select id, nome, stipendio from Dipendente")
    result = cur.fetchall()
    print("ID  | Nome |  Stipendio")
    for row in result:
        print("%s    %s    %d" % (row[0], row[1], row[2]))

    print("")
    print("Esempio 5: Select filtrata")
    cur.execute("select id, nome, stipendio from Dipendente where id in (2,3,4)")
    result = cur.fetchall()
    print("ID  | Nome |  Stipendio")
    for row in result:
        print("%s    %s    %d" % (row[0], row[1], row[2]))

    print("")
    print("Esempio 6: Select con order by")
    cur.execute("select id, nome, stipendio from Dipendente order by nome")
    result = cur.fetchall()
    print("ID  | Nome |  Stipendio")
    for row in result:
        print("%s    %s    %d" % (row[0], row[1], row[2]))

except:
    print("ERRORE")
    myconn.rollback()

myconn.close()