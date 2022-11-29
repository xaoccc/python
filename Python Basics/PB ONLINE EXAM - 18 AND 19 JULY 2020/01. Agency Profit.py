#input
company_name = input()
adult_tickets = int(input())
child_tickets = int(input())
adult_tickets_price = float(input())
service_price = float(input())
#putput
child_tickets_price = adult_tickets_price * 0.3
total_sales = (adult_tickets * adult_tickets_price) + (child_tickets * child_tickets_price) + ((adult_tickets + child_tickets) * service_price)
profit = total_sales * 0.2
#logic
print(f"The profit of your agency from {company_name} tickets is {profit:.2f} lv.")
