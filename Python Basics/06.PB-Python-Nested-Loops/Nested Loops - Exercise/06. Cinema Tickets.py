tickets_bought = 0
total_tickets_bought = 0
student_tickets_num = 0
standard_tickets_num = 0
kids_tickets_num = 0
while True:
    movie_name = input()
    if movie_name == "Finish":
        break
    free_seats = int(input())
    tickets_bought = 0
    while free_seats > tickets_bought:
        category = input()
        if category == "End":
            break
        if category == "student":
            student_tickets_num += 1
        elif category == "standard":
            standard_tickets_num += 1
        elif category == "kid":
            kids_tickets_num += 1
        tickets_bought += 1
    total_tickets_bought += tickets_bought
    fill_capacity = (tickets_bought / free_seats) * 100
    print(f"{movie_name} - {fill_capacity:.2f}% full.")
print(f"Total tickets: {total_tickets_bought}")
print(f"{(student_tickets_num / total_tickets_bought ) * 100:.2f}% student tickets.")
print(f"{(standard_tickets_num / total_tickets_bought ) * 100:.2f}% standard tickets.")
print(f"{(kids_tickets_num / total_tickets_bought ) * 100:.2f}% kids tickets.")


