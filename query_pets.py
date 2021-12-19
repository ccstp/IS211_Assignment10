import sqlite3


def check_user():
    conn = sqlite3.connect('pets.db')
    cur = conn.cursor()

    with conn:
        user_id = input("Enter user ID number. (Enter -1 to exit the program): ")
        while user_id != '-1':
            try:
                cur.execute("""
                SELECT first_name, 
                last_name, 
                person.age, 
                name, 
                breed, 
                dead, 
                pet.age
                FROM person_pet
                LEFT JOIN person ON person.id = person_pet.person_id
                LEFT JOIN pet ON pet.id = person_pet.pet_id
                WHERE person_id = ?""", user_id)

                results = cur.fetchall()

                if len(results) > 0:
                    for row in results:
                        print(f"{row[0]} {row[1]}, {row[2]} years old: ")
                        if row[5] == 0:
                            print(f"{row[0]} {row[1]} owns {row[3]}, a {row[4]}, that is {row[6]} years old.")
                        else:
                            print(f"{row[0]} {row[1]} owned {row[3]}, a {row[4]}, that was {row[6]} years old.")
                else:
                    print("There is no user with this ID. Please try again.")

                user_id = input("Enter user ID number: ")
            except:
                print("There is no user with this ID. Please try again.")


if __name__ == "__main__":
    check_user()
