size = int(input())
chars_list = []
max_count = 0
current_count = 0

for i in range(size):
    current_row = input().split()
    chars_list.append(current_row)

for i in range(len(chars_list)):
    if "." in chars_list[i]:
        for j in range(len(current_row)):
            if chars_list[i][j] == ".":
                current_count += 1
                if max_count < current_count:
                    max_count = current_count
            else:
                if i < len(chars_list) - 1:
                    if chars_list[i+1][j-1] == ".":
                        break
                    else:
                        if max_count < current_count:
                            max_count = current_count
                            current_count = 0
    else:
        current_count = 0 
                        
print(max_count)
