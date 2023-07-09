import sqlite3


# Setup Connection Database
db = sqlite3.connect("elzero.db")

# Setup Cursor 
cr = db.cursor()

# Create Table
cr.execute(f"CREATE TABLE if not exists users (user_id INTEGER UNIQUE, username TEXT UNIQUE, birthdate DATE UNIQUE, email TEXT UNIQUE)")

# Insert Data 
try :
    cr.execute(f"INSERT INTO users values(1,'Ahmed','20/10/1980','a@elzero.org')")
    cr.execute(f"INSERT INTO users values(2,'Sayed','20/10/1990','s@elzero.org')")
    cr.execute(f"INSERT INTO users values(3,'Gamal','05/10/1991','g@elzero.org')")
    cr.execute(f"INSERT INTO users values(4,'Mahmoud','09/10/1987','m@elzero.org')")
    cr.execute(f"INSERT INTO users values(5,'Sameh','08/11/2000','@elzero.org')")
except sqlite3.IntegrityError :
    print("This value is Already Defined")
    
# Retrive Data
cr.execute(f"SELECT * From users")
print(cr.fetchall()[-1])

cr.execute(f"SELECT * From users where user_id = 5")
print(cr.fetchone())


user_input = int(input("Enter User-ID : ").strip())

cr.execute(f"SELECT user_id From users")
id = []
for i in cr.fetchall() :
    id.append(i[0])
print(id)
if user_input in id:
    cr.execute(f"DELETE FROM users where user_id = {user_input}")
    print("Show Other Data:")
    cr.execute(f"SELECT * From users")
    for row in cr.fetchall() :
        print(f"ID => {row[0]}, Name => {row[1]}, Date Of Birth => {row[2]}, Email => {row[3]}")
else :
    print("User Not Found.")

# Save Changes
db.commit()

# Close Connection Database
db.close()