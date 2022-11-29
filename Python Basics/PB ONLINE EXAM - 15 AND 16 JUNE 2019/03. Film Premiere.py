movie = input()
movie_extras = input()
tickets = int(input())
 
if movie == "John Wick":
    if movie_extras == "Drink":
        ticket_price = 12
    elif movie_extras == "Popcorn":
        ticket_price = 15
    elif movie_extras == "Menu":
        ticket_price = 19
elif movie == "Star Wars":
    if movie_extras == "Drink":
        ticket_price = 18
    elif movie_extras == "Popcorn":
        ticket_price = 25
    elif movie_extras == "Menu":
        ticket_price = 30
elif movie == "Jumanji":
    if movie_extras == "Drink":
        ticket_price = 9
    elif movie_extras == "Popcorn":
        ticket_price = 11
    elif movie_extras == "Menu":
        ticket_price = 14
total_price = tickets * ticket_price
if tickets >= 4 and movie == "Star Wars":
    total_price *= 0.7
if tickets == 2 and movie == "Jumanji":
    total_price *= 0.85
 
print(f"Your bill is {total_price:.2f} leva.")
