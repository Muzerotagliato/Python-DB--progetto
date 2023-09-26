import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(host="localhost", user="root", passwd="root", database="negozio")

# creating the cursor object
cur = myconn.cursor()

try:
    """  # creiamo la nuova tabella per la join e inseriamo i dati
    cur.execute("create table Reparto (id_reparto int(20) primary key not null, nome_reparto varchar(40) not null)")
    insert = "insert into Reparto(id_reparto, nome_reparto) values (%s,%s)"
    val = [(201, "Generi Alimentari"), (202, "Generi Extralimentari")]
    cur.executemany(insert, val)
    print("Insert Reparto DONE")
    insert = "insert into Dipendente(id, nome, stipendio, ruolo, id_reparto) values (%s, %s, %s, %s, %s)"
    val = [(5,"Giuseppe", 25000.00, "Capo Reparto", 201),
           (6,"Luis", 25000.00, "Dipendente",202),
           (7,"Elton", 90000.00, "Amministratore", 201)]
    cur.executemany(insert, val)
    print("Insert Dipendenti DONE")
    # commit the transaction
    myconn.commit()"""

    print("")
    print("JOIN")
    cur.execute(
        "select Dipendente.id, Dipendente.nome, Dipendente.stipendio, Reparto.id_reparto, Reparto.nome_reparto "
        "from Reparto join Dipendente on Reparto.id_reparto = Dipendente.id_reparto")
    print("id_dipendente    Nome    Stipendio    id_reparto    nome_reparto")
    for row in cur:
        print("%d    %s    %d    %d    %s" % (row[0], row[1], row[2], row[3], row[4]))

    print("")
    print("RIGHT JOIN")
    result = cur.execute(
        "select Dipendente.id, Dipendente.nome, Dipendente.stipendio, Reparto.id_reparto, Reparto.nome_reparto from"
        " Reparto right join Dipendente on Reparto.id_reparto = Dipendente.id_reparto")
    print("id_dipendente    Nome    Stipendio    id_reparto    nome_reparto")

    for row in cur:
        print(row[0], "    ", row[1], "    ", row[2], "    ", row[3], "    ", row[4])

    print("")
    print("LEFT JOIN")
    result = cur.execute(
        "select Dipendente.id, Dipendente.nome, Dipendente.stipendio, Reparto.id_reparto, Reparto.nome_reparto from "
        "Reparto left join Dipendente on Reparto.id_reparto = Dipendente.id_reparto")
    print("id_dipendente    Nome    Stipendio    id_reparto    nome_reparto")
    for row in cur:
        print(row[0], "    ", row[1], "    ", row[2], "    ", row[3], "    ", row[4])


except:
    myconn.rollback()

myconn.close()