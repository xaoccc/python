age = float(input())
gen = input()

if gen == "f" and age < 16 :
    print ("Miss")
elif gen == "f" and age >= 16 :
    print ("Ms.")
elif gen == "m" and age < 16 :
    print ("Master")
elif gen == "m" and age >= 16 :
    print ("Mr.")