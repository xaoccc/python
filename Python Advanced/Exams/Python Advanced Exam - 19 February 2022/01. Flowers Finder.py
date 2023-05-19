from collections import deque
chars_one, chars_two = deque(input().split()), deque(input().split())
found = None
flowers = {
    "rose": "",
    "tulip": "",
    "lotus": "",
    "daffodil": ""
}
used_chars = []

while chars_one and chars_two and not found:
    vowel = chars_one.popleft()
    consonant = chars_two.pop()

    for key, value in flowers.items():
        if vowel in key and vowel not in used_chars:
            flowers[key] += vowel
            for k, v in flowers.items():
                if len(k) == len(v) and not found:
                    print(f"Word found: {key}")
                    found = key

        if consonant in key and consonant not in used_chars:
            if key == "daffodil" and (consonant == "f" or consonant == "d"):
                flowers[key] += consonant
            flowers[key] += consonant
            for k, v in flowers.items():
                if len(k) == len(v) and not found:
                    print(f"Word found: {key}")
                    found = key
    used_chars += [vowel, consonant]
if not found:
    print("Cannot find any word!")
if chars_one:
    print(f"Vowels left: {' '.join(chars_one)}")
if chars_two:
    print(f"Consonants left: {' '.join(chars_two)}")
