import re
text = input()
valid_data = []

data_test = re.findall(r'[#|][a-zA-Z ]+[|#]\d{2}\/\d{2}\/\d{2}[|#][0-9]+[#|]', text)
