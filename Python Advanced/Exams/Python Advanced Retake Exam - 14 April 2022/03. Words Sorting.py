def words_sorting(*args):
    words = {}
    result = ""
    for word in args:
        words[word] = sum([ord(i) for i in word])
    if sum(words.values()) % 2 != 0:
        words = dict(sorted(words.items(), key=lambda x: -x[1]))  
    else:
        words = dict(sorted(words.items(), key=lambda x: x[0]))  
    for key, value in words.items():
        result += f"{key} - {value}\n"
    return result
