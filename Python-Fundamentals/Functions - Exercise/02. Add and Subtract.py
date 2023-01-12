def add_and_subtract(num_one, num_two, num_three ):
    def sum_numbers():
        print(num_one + num_two)
    #HOW THE FUCK CAN I TAKE THE VALUE FROM sum_numbers AND USE IT IN subtract???
    def subtract():
        print(num_one + num_two - num_three)
    subtract()
add_and_subtract(int(input()), int(input()), int(input()))
