# this function removes spaces and new lines for column from right and left
def strip(string):
    return string.strip()

# this function reads database from contacts.txt file


def read_database():
    file = open("contacts.txt", encoding="utf-8")
    rows = []
    for row in file:
        rows.append(list(map(strip, row.split(", "))))
    return rows

# this function writes contacts to file


def write_database(db):
    file = open("contacts.txt", mode="w", encoding="utf-8")
    rows = []
    for row in db:
        rows.append(", ".join(row))
    file.write("\n".join(rows))
    file.close()

# this function prints all contacts from db that is in memory


def print_out_database(db):
    print("Index \t Name \t\t Phone \t\t Age \t Email")
    for i in range(0, len(db)):
        row = db[i]
        print(i, "\t", row[0], "\t", row[1], "\t", row[2], "\t", row[3], "\t")


def print_out_ages(db):
    sum = 0
    for i in range(0, len(db)):
        row = db[i]
        kolvo = len(db)
        sum = sum + int(row[2])
#        medium_age = sum + int(row[2]) / int(i)
    print(f"medium age is: {sum / kolvo}")


def print_out_commands():
    print("Commands are:")
    print("1. list users")
    print("2. edit user")
    print("3. add user")
    print("4. del user")


def main():
    db = read_database()
    print_out_database(db)
    print_out_ages(db)
    print_out_commands()


main()

command = input("What is your command?: ")

if command == "1":  # user list
    db = read_database()
    print_out_database(db)

if command == "4":  # user del
    condidat_na_vibivanie = int(input("Kakogo user'a udalit?(index): "))
    a_file = open("contacts.txt", "r", encoding="utf-8")
    lines = a_file.readlines()
    a_file.close()

    del lines[condidat_na_vibivanie]

    new_file = open("contacts.txt", "w+", encoding="utf-8")
    for line in lines:
        new_file.write(line)
    new_file.close()

if command == "3":  # user add
    a_file = open("contacts.txt", "r", encoding="utf-8")
    lines = a_file.readlines()
    a_file.close()

    name = input("name: ")
    phone = input("phone: ")
    age = input("age: ")
    email = input("email: ")
    user = (f"\n{name}, {phone}, {age}, {email}")

    new_file = open("contacts.txt", "a", encoding="utf-8")
    new_file.write(user)
    new_file.close()

if command == "2":  # edit user
    db = read_database()
    print_out_database(db)
    line = int(input("Kogo redachit?(index): "))
    param = int(
        input("Sto imenno menjat?\n 1. name\n 2. phone\n 3. age\n 4. email\n"))
    if param == 1:
        db = read_database()
        new_file = open("contacts.txt", "a", encoding="utf-8")
        new_name = input("new name: ")
        db[line][0] = new_name
        write_database(db)
    elif param == 2:
        db = read_database()
        new_file = open("contacts.txt", "a", encoding="utf-8")
        new_phone = input("new phone: ")
        db[line][1] = new_phone
        write_database(db)
    elif param == 3:
        db = read_database()
        new_file = open("contacts.txt", "a", encoding="utf-8")
        new_age = input("new age: ")
        db[line][2] = new_age
        write_database(db)
    elif param == 4:
        db = read_database()
        new_file = open("contacts.txt", "a", encoding="utf-8")
        new_email = input("new email: ")
        db[line][3] = new_email
        write_database(db)
