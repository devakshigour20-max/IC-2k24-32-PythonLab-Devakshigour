# Library Record System

books = {
    "B1": {"title": "Python Basics", "author": "Rao", "copies": 2, "issued_to": []},
    "B2": {"title": "Data Structures", "author": "Iyer", "copies": 1, "issued_to": []},
    "B3": {"title": "Algorithms", "author": "Rao", "copies": 1, "issued_to": []}
}

while True:
    print("\n1. Add book")
    print("2. Issue book")
    print("3. Return book")
    print("4. Search book")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        isbn = input("Enter ISBN: ")
        if isbn in books:
            copies = int(input("Enter extra copies: "))
            if copies > 0:
                books[isbn]["copies"] += copies
                print("Copies added")
            else:
                print("Enter a positive number")
        else:
            title = input("Enter title: ")
            author = input("Enter author: ")
            copies = int(input("Enter copies: "))
            if copies > 0:
                books[isbn] = {"title": title, "author": author,
                               "copies": copies, "issued_to": []}
                print("Book added")
            else:
                print("Enter a positive number")

    elif choice == "2":
        isbn = input("Enter ISBN: ")
        member = input("Enter member ID: ")
        if isbn not in books:
            print("Book not found")
        else:
            holdings = {}
            for book_id, book in books.items():
                for member_id in book["issued_to"]:
                    holdings.setdefault(member_id, []).append(book_id)

            book = books[isbn]
            if member in book["issued_to"]:
                print("Member already has this book")
            elif book["copies"] == 0:
                print("No copies available")
            elif len(holdings.get(member, [])) >= 2:
                print("Member already has two books")
            else:
                book["copies"] -= 1
                book["issued_to"].append(member)
                print("Book issued")

    elif choice == "3":
        isbn = input("Enter ISBN: ")
        member = input("Enter member ID: ")
        if isbn in books and member in books[isbn]["issued_to"]:
            books[isbn]["issued_to"].remove(member)
            books[isbn]["copies"] += 1
            print("Book returned")
        else:
            print("This member does not hold this book")

    elif choice == "4":
        isbn = input("Enter ISBN: ")
        print(books.get(isbn, "Book not found"))

    elif choice == "5":
        author = input("Enter author name: ")
        author_books = {isbn: book["title"] for isbn, book in books.items()
                        if book["author"].lower() == author.lower()}
        print("Books by author:", author_books)

        member_books = {}
        for isbn, book in books.items():
            for member in book["issued_to"]:
                member_books.setdefault(member, []).append(isbn)

        print("Members holding more than one book:",
              {member: ids for member, ids in member_books.items() if len(ids) > 1})

        print("Unavailable books:",
              {isbn: book["title"] for isbn, book in books.items() if book["copies"] == 0})
        print("Never issued:",
              {isbn: book["title"] for isbn, book in books.items()
               if len(book["issued_to"]) == 0})

    elif choice == "6":
        break
    else:
        print("Invalid choice")
