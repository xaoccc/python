playground, points = [], 0

for i in range(6):
    playground.append([int(i) if i.isdigit() else i for i in input().split()])

for i in range(3):
    throw = [int(i) for i in input()[1:-1].split(", ")]
    if throw[0] < 0 or throw[0] >= 6 or throw[1] < 0 or throw[1] >= 6 or playground[throw[0]][throw[1]] != "B":
        continue
    else:
        playground[throw[0]][throw[1]] = 0
        for row in range(6):
            points += playground[row][throw[1]]

if points > 299:
    prize = "Lego Construction Set"
elif 199 < points < 300:
    prize = "Teddy Bear"
elif 99 < points < 200:
    prize = "Football"
else:
    print(f"Sorry! You need {100 - points} points more to win a prize.")

if points > 99:
    print(f"Good job! You scored {points} points, and you've won {prize}.")
