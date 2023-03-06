text = input().lower()
chars_used, unique_chars_used, unique_chars_count = "", "", 0
result = ""

for i in range(len(text)):
    if text[i] not in unique_chars_used and not text[i].isdigit():
        unique_chars_used += text[i]
        unique_chars_count += 1
        
    if not text[i].isdigit():    
        chars_used += text[i]
        
    elif text[i].isdigit():
        if i < len(text)-1:
            if text[i+1].isdigit():
                result += chars_used.upper() * int(text[i]+text[i+1])
            else:
                result += chars_used.upper() * int(text[i])
        else:
            result += chars_used.upper() * int(text[i])
        chars_used = ""
    
print(f"Unique symbols used: {unique_chars_count}\n{result}")
