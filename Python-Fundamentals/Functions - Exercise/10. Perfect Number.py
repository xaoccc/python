def perfect_num(num_input = int(input())):
    num_check = 0
    for i in range(1, num_input):
        if num_input % i == 0:
            num_check += i
    if num_input == num_check:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")
perfect_num()
