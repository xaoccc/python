# valid date format: dd/mm/yyyy
def date_format_check(date_input):
    import re
    from datetime import datetime
    
    date_pattern = r'^(0[1-9]|1[012])\/(0[1-9]|[12][0-9]|3[01])\/(19|20)\d\d$'
    match = re.search(date_pattern, date_input)
    if match != None:
        date_string = match.string
        date_format = "%d/%m/%Y"
        datetime_object = datetime.strptime(date_string, date_format)
        return True
    else:
        print("Please enter a valid date fomat!")
        return False
