def factorial(num_one, num_two, _num_one, _num_two):
    for i in range(1, num_one + 1):
        _num_one *= i
    for j in range(1, num_two + 1):
        _num_two *= j
    print(f"{_num_one / _num_two :.2f}")
factorial(int(input()), int(input()), 1, 1)
