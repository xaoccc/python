favourite_book = input()
book_num = 0
book = ""

while book != favourite_book:
    book = input()
    if book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {book_num} books.")
        break
    book_num += 1
if book == favourite_book: 
    print(f"You checked {book_num-1} books and found it.")