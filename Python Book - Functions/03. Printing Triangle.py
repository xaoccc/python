def print_line(start, end):
    for i in range(start, end + 1):
      #Reference -> space , same line      
        print(str(i) + " ", end="")
    print("")
    
n = int(input())    

for i in range(0, n):
  # Call the function n-1 times(first argument is 1)
  # First call prints "1"
  # Second call: "1 2" <- note that 1 and 2 (see Reference) are separated with space and on the same line
  # Last call prints "1 2 3... n-1"
  # In the end of the function, we print a blank line, so the next call is on a new line
    print_line(1, i)

# Call the function 1 time with all numbers from 1 to n (inclusive -> end + 1 in function)
print_line(1, n)


for i in range(n - 1, -1, -1):
  # Call the function n-1 times with the same arguments as before, but reversed order
  # First call prints "1 2 3... n-1"...
  # Last call prints "1"
    print_line(1, i)  
