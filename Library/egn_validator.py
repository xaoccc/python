from datetime import datetime

def egn_validator():
    egn = input()
    if len(egn) != 10:
        return "EGN must be exactly ten digits."
    elif not egn.isdigit():
        return "EGN must not contain other symbols than digits."
    
    date_string = egn[:6]
    if date_string[2] == "4" or date_string[2] == "5":
        date_string = date_string[:2] + str(int(date_string[2]) - 4) + date_string[3:]
        date_string = "20" + date_string
    elif date_string[2] == "0" or date_string[2] == "1":
        date_string = "19" + date_string
    else:
        return "Invalid EGN format!"
    
    try:
        birthdate = datetime.strptime(date_string, '%Y%m%d')
        return egn
    except ValueError:
        return "Invalid birth date!"
