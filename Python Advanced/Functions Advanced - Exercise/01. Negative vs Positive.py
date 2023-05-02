def negative_positive(*nums):
    negative, positive = 0, 0
    for num in nums:
        if num < 0:
            negative += num
        else:
            positive += num
    print(negative)
    print(positive)
    if abs(negative) > positive:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")    
    
negative_positive(*[int(i) for i in input().split()])
