import sqlite3

db = sqlite3.connect("contacts.db")
update_cursor = db.cursor()

new_email = input("Email : ")
phone = input("Phone : ")

update_sql = "UPDATE contacts SET email = '{0}' WHERE phone = {1}"\
    .format(new_email, phone)
print(update_sql)

update_cursor.executescript(update_sql)
print("{} rows updated".format(update_cursor.rowcount))

update_cursor.connection.commit()
update_cursor.close()




