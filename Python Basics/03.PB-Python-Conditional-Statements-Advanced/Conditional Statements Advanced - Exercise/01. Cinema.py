#user input
projection = input().lower()
rows = int(input())
columns = int(input())

#logic and output
cinema_size = rows * columns
if  projection == "premiere" :
    ticket_price = 12
    print (f"{ticket_price * cinema_size:.2f} leva")
elif  projection == "normal" :
    ticket_price = 7.5
    print (f"{ticket_price * cinema_size:.2f} leva")
elif  projection == "discount" :
    ticket_price = 5
    print (f"{ticket_price * cinema_size:.2f} leva")