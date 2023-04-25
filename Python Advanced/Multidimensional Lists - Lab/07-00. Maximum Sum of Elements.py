#This program find the biggest sum of two pairs of elements in a matrix, prints them and their total sum 

import copy
matrix_size = [int(i) for i in input().split(", ")]
matrix = []
final_matrix = []
total = 0
final_rows_count = 0
sum_list = []

if matrix_size[0] == 1:
    matrix.append([int(i) for i in input().split(", ")])
    original_matrix = copy.deepcopy(matrix)
    matrix[0].sort()
    biggest_num = max(matrix[0])
    second_biggest_num = matrix[0][-2]
    if original_matrix[0].index(biggest_num) < original_matrix[0].index(second_biggest_num):
        print(biggest_num)
        print(second_biggest_num)
    else:
        print(second_biggest_num)
        print(biggest_num)
    print(matrix[0][-1] + matrix[0][-2])
    
else:
    for i in range(matrix_size[0]):
        matrix.append([int(j) for j in input().split(", ")])
    original_matrix = copy.deepcopy(matrix)

    for i in range(matrix_size[0]):
        biggest_num = max(matrix[i])
        matrix[i].sort()
        second_biggest_num = matrix[i][-2]
        if original_matrix[i].index(biggest_num) < original_matrix[i].index(second_biggest_num):
            final_matrix.append([biggest_num, second_biggest_num])
        else:
            final_matrix.append([second_biggest_num, biggest_num])
    
    if matrix_size[0] == 2:
        for row in final_matrix:
            total += sum(row)
            print(*row)
        print(total)
        
    else:
        for nums in final_matrix:
            sum_list.append(sum(nums))
        sum_list.sort()
        for i in final_matrix:
            if sum(i) == sum_list[-1] or sum(i) == sum_list[-2]:
                total += sum(i)
                print(*i)
                final_rows_count += 1
                if final_rows_count == 2:
                    break
        print(total)
