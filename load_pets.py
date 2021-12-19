import sqlite3

conn = sqlite3.connect('pets.db')
cur = conn.cursor()

person = (
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
)

pet = (
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
)

person_pet = (
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
)

cur.execute("DROP TABLE IF EXISTS person")
cur.execute("DROP TABLE IF EXISTS pet")
cur.execute("DROP TABLE IF EXISTS person_pet")

cur.execute("CREATE TABLE person(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER)")
cur.execute("CREATE TABLE pet(id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER, dead INTEGER)")
cur.execute("CREATE TABLE person_pet(person_id INTEGER, pet_id INTEGER)")

conn.commit()

if __name__ == "__main__":
    cur = conn.cursor()

    cur.executemany("INSERT INTO person VALUES (? , ? , ? , ? )", person)
    cur.executemany("INSERT INTO pet VALUES (?, ?, ?, ?, ?)", pet)
    cur.executemany("INSERT INTO person_pet VALUES (?, ?)", person_pet)

    conn.commit()
    conn.close()

"""
Part 2
'What is the purpose of the person_pet table?'

The purpose of the person_pet table, known as a junction table, is to cross references the person table with the pet
table. Junction tables are often used when there is a many-to-many relationship between tables.
"""
