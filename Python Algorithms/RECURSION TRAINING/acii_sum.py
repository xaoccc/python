def acii_sum(word, idx, ord_sum):
    ord_sum += ord(word[idx])
    if idx == len(word) - 1:
        return print(ord_sum)
    else:
        acii_sum(word, idx + 1, ord_sum)
    
acii_sum(input(), 0, 0) 
