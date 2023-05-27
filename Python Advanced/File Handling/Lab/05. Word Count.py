try:
    with open("words.txt", "r") as words:
        with open("text.txt", "r") as file:
            text = " ".join([i[:-1] for i in file.readlines()]).lower()
            words = words.read().lower().split()
            for word in words:
                print(f"{word} - {text.count(word)}")
except FileNotFoundError:
    print("File not found!")