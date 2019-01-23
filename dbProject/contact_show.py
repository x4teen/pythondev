import sqlite3

db = sqlite3.connect("contacts.db")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

for name, phone, email in cursor:
    print("Name= {0}\tPhone= {1}\tEmail= {2}"
          .format(name, phone, email))

cursor.close()

db.close()

