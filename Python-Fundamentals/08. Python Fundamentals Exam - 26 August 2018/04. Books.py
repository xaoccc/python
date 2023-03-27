import re

book = input()
all_books = {}
sold_books = []
money_collected = 0

while book != "on work":
    book = book.split(" -> ")
    book[0] = book[0].split()
    book[1] = book[1].split(", ")

    if len(book[0]) == 3:
        match = re.match(r"^\d+\.\d+$|^\d+$", book[0][2])
        if match:
            book_name = book[0][0]
            book_author = book[0][1]
            book_price = float(book[0][2])
            chapters = book[1]
            if book_name not in all_books and book_price > 0:
                all_books[book_name] = [book_author, book_price, chapters]

    book = input()

command = input()
while command != "end work":
    found = False
    for book, book_info in all_books.items():
        if book == command:
            found = True
            break
    if not found:
        print("No such book here")
    else:
        sold_books.append([command, all_books[command][0], all_books[command][1], all_books[command][2]])
        money_collected += all_books[command][1]

    command = input()

for book in sold_books:
    print(f"SOLD: {book[0]} with author {book[1]}. Chapters in the book {len(book[3])}")

if len(sold_books) > 0:
    print(f"Money: {money_collected:.2f}")
else:
    print("Bad day :(")
    
    
# import re
# books, sold_books, money_collected = {}, [], 0
# pattern = r"(?P<name>[a-zA-Z0-9]+) +(?P<author>[a-zA-Z0-9]+) +(?P<price>([0-9]+\.[0-9]+)|([0-9]+)) "

# book = input()
# while book != "on work":
#     book = book.split("-> ")
#     book_name, author, price = None, None, None
#     match = re.finditer(pattern, book[0])
#     for i in match:
#         book_name = i["name"]
#         author = i["author"]
#         price = float(i["price"])
#     if author and price > 0 and book_name:
#         chapters = book[1].split(", ")
#         books[book_name] = [author, price, chapters]
#     book = input()

# command = input()
# while command != "end work":
#     if command not in books.keys():
#         print("No such book here")
#     else:
#         sold_books.append([command, books[command][0], books[command][1], books[command][2]])
#         money_collected += books[command][1]
#     command = input()

# for book in sold_books:
#     print(f"SOLD: {book[0]} with author {book[1]}. Chapters in the book {len(book[3])}")

# if len(sold_books) > 0:
#     print(f"Money: {money_collected:.2f}")
# else:
#     print("Bad day :(")
