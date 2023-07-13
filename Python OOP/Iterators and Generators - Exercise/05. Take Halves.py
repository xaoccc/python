def solution():
    def integers():
        i = 0
        while True:
            yield i
            i += 1

    def halves():
        for i in integers():
            yield i / 2

    # TODO: Implement
    def take(n, seq):
        m = 0
        while m <  n:
            yield seq[m]
            m += 1

    # TODO: Implement
    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

