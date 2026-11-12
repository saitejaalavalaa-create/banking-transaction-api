import sqlite3
connection = sqlite3.connect("banking.db")
cursor = connection.execute("SELECT * FROM accounts WHERE account_id = ?", (99,))
account = cursor.fetchone()
print("Selected account", account)
connection.close()