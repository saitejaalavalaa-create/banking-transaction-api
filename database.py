import sqlite3

connection = sqlite3.connect("banking.db")

print("Datbase connection successful")

connection.execute("""
create table if not exists accounts( 
account_id integer primary key,
name text not null,
balance_cents integer not null default 0)  """)

connection.execute( "insert into accounts (name, balance_cents) values (?, ?)",("John Doe", 10000))
connection.commit()

cursor = connection.execute("select * from accounts")
rows = cursor.fetchall()
print("Bank accounts:", rows)

connection.close()
