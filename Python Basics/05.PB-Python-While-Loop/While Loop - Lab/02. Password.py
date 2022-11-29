#user input
user_name = input()
password = input()
#here we define the correct password as a variable
correct_password = input()

#here we check if the password written is the same as the correct one
while password != correct_password :
    correct_password = input()
#output. 
#If we put print() inside the loop, the program will greet you everytime, even when the password is wrong. 
#If we put print() at the beginning of the loop, just before correct_password = input(), the program will greet you every time you write a wrong password and not greet you when the password is correct. 
print(f"Welcome {user_name}!")