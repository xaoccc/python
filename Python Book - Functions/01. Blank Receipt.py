def print_receipt_header():
    print("CASH RECEIPT")
    print("------------------------------")
def print_receipt_body():
    print("Charged to____________________")
    print("Received by___________________")
def print_receipt_bottom():
    print("------------------------------")
    print("(c) SoftUni")

def print_receipt():
    print_receipt_header()
    print_receipt_body()
    print_receipt_bottom()
print_receipt()
