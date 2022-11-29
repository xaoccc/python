pair1 = int(input())
pair2 = int(input())
diff_pair1 = int(input())
diff_pair2 = int(input())
is_num_1_prime = False
is_num_2_prime = False

#We are checking for two numbers in each range (pair1 or 2  < prime number < pair1 or 2 + diff_pair1 or 2)
for prime_num_1 in range(pair1, pair1 + diff_pair1 + 1):  
  for prime_num_2 in range(pair2, pair2 + diff_pair2 + 1):
#Here we assume all the numbers in range 1 are prime  
    is_num_1_prime = True
#If the conditions for the 1st number for prime are not met, then we break the loop
    if prime_num_1 > 1:
      for i in range(2, prime_num_1):
        if (prime_num_1 % i) == 0:
          is_num_1_prime = False
          break 
      
#We are doing the same check for the second number, as we store the results in the variables is_num_1_prime and is_num_2_prime     
    if prime_num_2 > 1:    
      is_num_2_prime = True
      for j in range(2, prime_num_2):
        if (prime_num_2 % j) == 0:
          is_num_2_prime = False
          break   
#Output          
    if is_num_1_prime and is_num_2_prime: 
      print(str(prime_num_1) + str(prime_num_2))
          

