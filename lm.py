# ---------------- LOGIN AUTHENTICATION ----------------

USERNAME = "admin"
PASSWORD = "admin123"

print("=" * 50)
print("      LIBRARY MANAGEMENT SYSTEM")
print("=" * 50)

attempts = 3

while attempts > 0:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == USERNAME and password == PASSWORD:
        print("\nLogin Successful!\n")
        break
    else:
        attempts -= 1
        print("Invalid Username or Password")
        print("Attempts Left:", attempts)

if attempts == 0:
    print("Access Denied!")
    exit()

# ---------------- LIBRARY DATABASE ----------------

books = {}

while True:

    print("\n========== LIBRARY MENU ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        book_id = input("Enter Book ID: ")

        if book_id in books:
            print("Book already exists!")

        else:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            books[book_id] = {
                "Title": title,
                "Author": author,
                "Issued": False
            }

            print("Book Added Successfully!")

    elif choice == "2":

        if len(books) == 0:
            print("No Books Available!")

        else:

            print("\n========== BOOK LIST ==========")

            for book_id, details in books.items():

                status = "Issued" if details["Issued"] else "Available"

                print("Book ID :", book_id)
                print("Title   :", details["Title"])
                print("Author  :", details["Author"])
                print("Status  :", status)
                print("-" * 35)

    elif choice == "3":

        book_id = input("Enter Book ID: ")

        if book_id in books:

            status = "Issued" if books[book_id]["Issued"] else "Available"

            print("\nBook Found")
            print("Title  :", books[book_id]["Title"])
            print("Author :", books[book_id]["Author"])
            print("Status :", status)

        else:
            print("Book Not Found!")

    elif choice == "4":

        book_id = input("Enter Book ID: ")

        if book_id in books:

            if books[book_id]["Issued"]:
                print("Book Already Issued!")

            else:
                books[book_id]["Issued"] = True
                print("Book Issued Successfully!")

        else:
            print("Book Not Found!")

    elif choice == "5":

        book_id = input("Enter Book ID: ")

        if book_id in books:

            if books[book_id]["Issued"]:
                books[book_id]["Issued"] = False
                print("Book Returned Successfully!")

            else:
                print("Book Was Not Issued!")

        else:
            print("Book Not Found!")

    elif choice == "6":

        book_id = input("Enter Book ID: ")

        if book_id in books:

            del books[book_id]
            print("Book Deleted Successfully!")

        else:
            print("Book Not Found!")

    elif choice == "7":

        print("Thank You!")
        break

    else:

        print("Invalid Choice!")