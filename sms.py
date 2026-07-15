# ---------------- LOGIN AUTHENTICATION ----------------

USERNAME = "admin"
PASSWORD = "admin123"

print("=" * 50)
print("     STUDENT MANAGEMENT SYSTEM")
print("=" * 50)

attempts = 3

while attempts > 0:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == USERNAME and password == PASSWORD:
        print("\nLogin Successful!")
        break
    else:
        attempts -= 1
        print("\nInvalid Username or Password.")
        if attempts > 0:
            print("Attempts Remaining:", attempts)

if attempts == 0:
    print("\nToo many failed attempts.")
    print("Access Denied!")
    exit()

# ---------------- STUDENT MANAGEMENT SYSTEM ----------------

students = {}

while True:

    print("\n" + "=" * 50)
    print("        STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    # ---------------- ADD STUDENT ----------------

    if choice == "1":

        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Student already exists!")

        else:
            name = input("Enter Student Name: ")
            age = input("Enter Age: ")
            branch = input("Enter Branch: ")
            marks = input("Enter Marks: ")

            students[roll] = {
                "Name": name,
                "Age": age,
                "Branch": branch,
                "Marks": marks
            }

            print("\nStudent Added Successfully!")

    # ---------------- VIEW STUDENTS ----------------

    elif choice == "2":

        if len(students) == 0:
            print("\nNo Student Records Found!")

        else:

            print("\n========== STUDENT RECORDS ==========")

            for roll, details in students.items():

                print("\nRoll Number :", roll)
                print("Name        :", details["Name"])
                print("Age         :", details["Age"])
                print("Branch      :", details["Branch"])
                print("Marks       :", details["Marks"])
                print("-" * 35)

    # ---------------- SEARCH STUDENT ----------------

    elif choice == "3":

        roll = input("Enter Roll Number to Search: ")

        if roll in students:

            print("\nStudent Found")

            print("Roll Number :", roll)
            print("Name        :", students[roll]["Name"])
            print("Age         :", students[roll]["Age"])
            print("Branch      :", students[roll]["Branch"])
            print("Marks       :", students[roll]["Marks"])

        else:
            print("Student Not Found!")

    # ---------------- UPDATE STUDENT ----------------

    elif choice == "4":

        roll = input("Enter Roll Number to Update: ")

        if roll in students:

            print("\nEnter New Details")

            students[roll]["Name"] = input("New Name: ")
            students[roll]["Age"] = input("New Age: ")
            students[roll]["Branch"] = input("New Branch: ")
            students[roll]["Marks"] = input("New Marks: ")

            print("\nStudent Updated Successfully!")

        else:
            print("Student Not Found!")

    # ---------------- DELETE STUDENT ----------------

    elif choice == "5":

        roll = input("Enter Roll Number to Delete: ")

        if roll in students:

            del students[roll]

            print("\nStudent Deleted Successfully!")

        else:
            print("Student Not Found!")

    # ---------------- EXIT ----------------

    elif choice == "6":

        print("\nThank You for Using Student Management System.")
        break

    # ---------------- INVALID ----------------

    else:

        print("\nInvalid Choice!")
        print("Please Enter a Number Between 1 and 6.")