searched_book = str(input())
checked = str(input())


checked_books = 0

while checked != searched_book and checked != "No More Books":
    checked_books += 1

    checked = str(input())

if checked == searched_book:
    print(f"You checked {checked_books} books and found it.")
elif checked == "No More Books":
    print(f"The book you search is not here!")
    print(f"You checked {checked_books} books.")

