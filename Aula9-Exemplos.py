import mysql.connector

mydb=mysql.connector.connect( host="localhost", user="root",password="Fortun@9", database="ipt2023")

#print(mydb)
mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE IPT2023")
#
# for x in mycursor:
#     print(x)

#mycursor.execute("CREATE TABLE customers(name VARCHAR(255),address VARCHAR(255))") #Criar tabela com campos

# -----------mostra todasa as tabelas-----------
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# -----------Inserir uma linha com contagem de linha-----------
# sql="INSERT INTO customers (name,address) VALUES(%s,%s)"
# val=("Jonhn","Highway21")
# mycursor.execute(sql,val)
# mydb.commit() #aplica as alaterações à BD a todos os utlizadores
#
# print(mycursor.rowcount,"Record inserted.")

#-----------Inserir multiplos dados -----------
# sql="INSERT INTO customers (name,address) VALUES(%s,%s)"
# val=[("Peter","Lowes4"),("Amy","Apple st 652"),("Hannah","Mountain 21"),("Michael","Vally345"),("Sandy","Ocean blvd2"),
#      ("Betty","Green Grass1"),("Richard","Sky st 331"),("Susan","One way 98"),("Vicky","Yellow Garden2"),("Ben","Park Lane 38"),
#      ("William","Central t 954"),("Chuck","Main Road 989"),("Viola","Sidedeway 1633")]
# mycursor.executemany(sql,val)
# mydb.commit() #aplica as alaterações à BD a todos os utlizadores
#
# print(mycursor.rowcount,"was inserted.")

# -----------Inserir uma linha com obtnção do id -----------
# sql="INSERT INTO customers (name,address) VALUES(%s,%s)"
# val=("Michelle","Blue Village")
# mycursor.execute(sql,val)
# mydb.commit()
# print("1 record inserted, ID:", mycursor.lastrowid)

# -----------Lista o conteudo completo numa tabela temporária e em seguida é efetuada consulta à tablela temporária-----------
# mycursor.execute("SELECT * FROM customers")
# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)


#-----------Lista o conteudo especificado numa tabela temporária e em seguida é efetuada consulta à tablela temporária-----------
# mycursor.execute("SELECT name,address FROM customers")
# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)

#-----------Lista o conteudo especificado numa tabela temporária e em seguida é efetuada consulta ao primeiro da lista-----------
# mycursor.execute("SELECT * FROM customers")
# myresult=mycursor.fetchone()
# print(myresult)

#-----------Lista o conteudo especificado numa tabela temporária e em seguida é efetuada consulta com filtros à tablela temporária-----------
# sql="SELECT * FROM customers WHERE address = 'Park Lane 38'"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)

#-----------Lista o conteudo especificado numa tabela temporária e em seguida é efetuada consulta usando % à tablela temporária----------
# sql="SELECT * FROM customers WHERE address LIKE'%way%'"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# for x in myresult:
#    print(x)

#-----------Lista o conteudo especificado numa tabela temporária e em seguida é efetuada consulta usando  ORDENAÇÃO à tablela temporária----------
# sql="SELECT * FROM customers ORDER BY name"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# for x in myresult:
#  print(x)


#-----------Lista o conteudo especificado numa tabela temporária e em seguida é efetuada consulta upara limpar registos à tablela----------
# sql="DELETE FROM customers WHERE address='Mountain 21"
# mycursor.execute(sql)
# mydb.commit
# print(mycursor.rowcount,"records deleted")


#----------- Apagar a tabela-----------
# mycursor=mydb.cursor()
# sql="DROP TABLE customers"
# mycursor.execute(sql)

#----------- Apagar a tabela apenas se existir-----------
# mycursor=mydb.cursor()
# sql="DROP TABLE IF EXISTS customers"
# mycursor.execute(sql)

#----------- Atualizar a tabela apenas se existir-----------
# mycursor=mydb.cursor()
# sql="DROP TABLE IF EXISTS customers"
# mycursor.execute(sql)


#----------- UPDATE localizado-----------
# sql="UPDATE customers SET address = 'Canyon 123'WHERE address = 'Vally345'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"records affected")

#----------- Atualizar a tabela apenas se existir----------- FALTA COMPLETAR
# mycursor=mydb.cursor()
# sql="UPDATE customers SET address = %s WHERE address=%s"
# val=("Valley 345", "Canyon 123")

#----------- Limitar resultados-----------
# mycursor.execute("SELECT * FROM customers LIMIT 5")
# myresult=mycursor.fetchall()
# for x in myresult:
#  print(x)

#----------- Limitar resultados começando noutra posição-----------
# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
# myresult=mycursor.fetchall()
# for x in myresult:
#  print(x)

#----------- Junção de tabelas com JOIN ou INNER JOIN-----------

#----------- Junção de tabelas com LEFT JOIN e RIGHT JOIN-----------

#----------- Inserir data e hora-----------
# from datetime import datetime
# now=datetime.now()
# id=1
# formatted_date=now.strftime('%Y-%m-%d %H:%M:%S')
#
# cursor.execute(insert into table(id,date_created) values(%s,%s), (id,formatted_date))





