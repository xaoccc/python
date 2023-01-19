def tribunacci(num = int(input())):
  #this works out for n-bonacci sequences, the if-else statemnts will always be n+1
    if num == 1:
        print(1)
    elif num == 2:
        print("1 1")
    elif num == 3:
        print("1 1 2")
    else:
        #This is the n-th sequence and we start from here, len(trib_seq) == n, the range will be num-n, as num is the given number of sequences and n is the number if numbers to be summed, 
        #for example, in fibonacci n==2, tribonacci n==3, etc.
        trib_seq = [1, 1, 2]
        for i in range(num-3):
          #For each new element of the list we add a n number of prevoius elemnts (2, 3 or more), here you see 3 elements, as this is a tri(3)bonacci sequence
            trib_seq.append(trib_seq[i] + trib_seq[i+1] + trib_seq[i+2])
        #When the list is ready, we can format it to whatever we like. Here we need a single string of numbers, divided by space
        trib_seq = " ".join(list(map(str, trib_seq)))
        print(trib_seq)
tribunacci()
