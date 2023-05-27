try:
    file = open("text.txt")
    print("File found")
    file.close()
except FileNotFoundError:
    print("File not found")