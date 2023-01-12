#data input
grade_data = float(input())

#create function with 1 parameter we use for if-else checks and use return which exits the function
def grades(grade):
    if 2 <= grade < 3:
        return "Fail"
    elif 3 <= grade <= 3.49:
        return "Poor"
    elif 3.5 <= grade <= 4.49:
        return "Good"
    elif 4.5 <= grade <= 5.49:
        return "Very Good"
    else:
        return "Excellent"
        
#output - we print the function result and instead of the parameter, we write the input, which gives value to the initially creatd parameter, otherwise we have no data to check
print(grades(grade_data))
