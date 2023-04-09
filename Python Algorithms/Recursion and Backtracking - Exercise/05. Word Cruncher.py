


words = input().split(", ")
target = input()

words_by_idx = {}
words_count = {}

for word in words:
    if word in words_by_idx:
        words_by_idx[word] += 1
    else:
        words_by_idx[word] = 1

    try:
        idx = 0
        while True:
            idx = target.index(word, idx)
            if idx not in
    except ValueError:
        pass



# def word_crunch(idx, text,  strings, result):
#     if idx == len(strings):
#         return
#     if text.startswith(strings[idx]):
#         text = text[len(strings[idx]):]
#         result.append(strings[idx] + " ")
#
#     word_crunch(idx + 1, text, strings, result)
#
#     return result
#
# strings = input().split(", ")
# text = input()
# result = []
#
# print(word_crunch(0, text, strings, result))