from datetime import datetime

guests_num = int(input())
start = datetime.now()
guests_list = []
guests_arrived = []

while len(set(guests_list)) < guests_num:
    code = input()
    if len(code) == 8:
        guests_list.append(code)

code = input()
while code != "END":
    if len(code) == 8:
        guests_arrived.append(code)
    code = input()

result = sorted(set(guests_list) - set(guests_arrived))
print(len(result))
print(*result, sep="\n")
end = datetime.now()
print(end - start)

# n = int(input())
# start = datetime.now()
# reservations = set()
#
# for i in range(n):
#     reservation_num = input()
#     reservations.add(reservation_num)
#
# guest_reservation_num = input()
# while guest_reservation_num != "END":
#     reservations.remove(guest_reservation_num)
#     guest_reservation_num = input()
#
# print(len(reservations))
# for num in sorted(reservations):
#     print(num)
#
# end = datetime.now()
# print(end - start)
