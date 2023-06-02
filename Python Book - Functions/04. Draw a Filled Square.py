def print_header_footer(n):
    print("-" * n * 2)
    
def print_body(n):
    print("-", end="")
    for i in range((n - 1) * 2):
        if i % 2 == 0:
            print("\\", end="")
        else:
            print("/", end="")
    print("-")

def print_square(n):
    print_header_footer(n)
    for i in range(n - 2):
        print_body(n)
    print_header_footer(n)

n = int(input())

print_square(n)
