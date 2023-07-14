def solution():
    def integers():
        i = 1
        while True:
            yield i
            i += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for i in range(n):
            result.append(next(seq))
        return result


    return (take, halves, integers)

