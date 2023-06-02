def print_sign(n):
    if n == 0:
        print("The number 0 is zero.")
    else:
        print(f"The number {n} is {'positive' if n > 0 else 'negative'}.")

print_sign(int(input()))
