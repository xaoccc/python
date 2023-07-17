def number_increment(numbers):
    def increase():
        return [i+1 for i in numbers]
    return increase()
