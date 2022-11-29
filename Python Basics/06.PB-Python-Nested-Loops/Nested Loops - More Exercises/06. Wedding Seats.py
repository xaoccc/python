sector = input()
rows_sector = int(input())
places_num_odd_row = int(input())

sector = ord(sector)
sector_name = ""
seats_num = 0
seats = 0

for i in range(65, sector + 1):
    rows_sector += 1
    sector_name = chr(i)
    for j in range(1, rows_sector):
        if j % 2 == 0:
            seats_num = places_num_odd_row + 2
        else:
            seats_num = places_num_odd_row
        for k in range(97, seats_num + 97):
            seats += 1
            place = chr(k)
            print(sector_name + str(j) + place)
print(seats)