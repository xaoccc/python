import re

barcodes_num = int(input())
pattern = r'@[#]+[A-Z][a-zA-Z0-9]{4,}[A-Z]@[#]+'
find_digits_in = r'[0-9]+'

for i in range(barcodes_num):
    barcode = input()
    barcode_check = re.findall(pattern, barcode)
    digits_check = re.findall(find_digits_in, barcode)
    if len(barcode_check) > 0:
        if len(digits_check) == 0:
            print("Product group: 00")
        else:
            print(f"Product group: {''.join(digits_check)}")
    else:
        print("Invalid barcode")