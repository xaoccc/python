try:
    file = open("text.txt", "r")
    print("File found")
    file.close()
except FileNotFoundError:
    print("File not found")