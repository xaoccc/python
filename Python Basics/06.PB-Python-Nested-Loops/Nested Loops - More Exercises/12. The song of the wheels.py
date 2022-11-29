control_value = int(input())
counter = 0
password = 0
pass_found = False

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if control_value == (a * b) + (c * d) and a < b and c > d:
                    counter += 1
                    output = f"{a}{b}{c}{d}"
                    if counter == 4:
                        pass_found = True
                        password = output
                    print(output, end=" ")
if pass_found:
    print("\nPassword: " + password)
else:
    print("\nNo!")