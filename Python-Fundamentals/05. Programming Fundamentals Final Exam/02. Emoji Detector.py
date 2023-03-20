import re
text = input()
cool_threshold, cool_emojis, emojis_count = 1, [], 0
pattern = r"(::|\*\*)[A-Z][a-z]{2,}\1"
match = re.finditer(pattern, text)

for num in text:
    if num.isdigit():
        cool_threshold *= int(num)
for emoji in match:
    emojis_count += 1
    emoji_coolness = 0
    for char in emoji.group():
        emoji_coolness += ord(char)
    if emoji_coolness >= cool_threshold:
        cool_emojis.append(emoji.group())
print(f"Cool threshold: {cool_threshold}\n{emojis_count} emojis found in the text. The cool ones are:")
for i in cool_emojis:
    print(i)

