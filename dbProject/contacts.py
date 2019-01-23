import sqlite3

db = sqlite3.connect("contacts.db")
db.execute("CREATE TABLE IF NOT EXISTS "
           "contacts(name TEXT, phone INTEGER, email TEXT)")


def add_contact(connection, tbl_name, name, phone=None, email=None):
    sql_command = "INSERT INTO {0} (name, phone, email)"\
        .format(tbl_name)
    sql_command += " VALUES('{0}', {1}, '{2}')"\
        .format(name, phone, email)
    connection.execute(sql_command)
    return sql_command


add_contact(db, 'contacts', 'Tim', 654678, 'tim@gmail.com')
add_contact(db, 'contacts', 'Brian', 1234, 'brian@gmail.com')
add_contact(db, 'contacts', 'Ryan', 12345, 'ryank@gmail.com')

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
print(cursor.fetchone())
print(cursor.fetchone())

for name, phone, email in cursor:
    print("Name= {0}\tPhone= {1}\tEmail= {2}"
          .format(name, phone, email))

print(cursor.fetchone())
print(cursor.fetchone())
cursor.close()
db.commit()
db.close()

