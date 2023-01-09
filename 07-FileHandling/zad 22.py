import csv
with open("students.txt", newline='') as file:
    read = csv.DictReader(file)
    for row in read:
        age = row['age']
        if int(age) < 30:
            print(f"{row['first_name']} {row['last_name']} {row['email']}")
file.close()
