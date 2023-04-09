# Split the first input into a list
words = input().split(", ")
target = input()

# Create a dictionary for the indexes of the possible target parts
words_by_idx = {}
# Count how many times each word part repeats in the first input
words_count = {}

for word in words:
    # Collecting all info for the dictionary words_count{}
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1

    try:
        # Counting and collectin info for each word part contained in the target, starting from index 0
        idx = 0
        while True:
            # Find the first occurence of the substring
            idx = target.index(word, idx)
            # If this is its first occurence, we add it to the dictionary first by creating the index as key
            if idx not in words_by_idx:
                words_by_idx[idx] = []
            # Then adding the substring as value. Values of dict words_by_idx are lists, so we use append()
            # We do this to prevent adding the same substring multiple times and creating multiple equal outputs
            if word not in words_by_idx[idx]:
                words_by_idx[idx].append(word)
            # After we do this check, we change the index, because we have already checked everything until the end
            # of this substring
            idx += len(word)
    # Here we escape the Error message
    except ValueError:
        pass
# At this point we have info about all positions of all valid substrings and their count in the first input
# Now using recursion and backtracking we have to find all valid combinations of substrings forming the target string

def findallsolutions(idx, target, words_by_idx,  words_count, used_words):
    # If the lenght of found combination is the same as target's, this means we have found a solution
    if len("".join(used_words)) == len(target):
        # So we print the solution
        print(" ".join(used_words))
        return

    # Here we check is there are remaining any valid solutions in our dictionary words_by_idx
    if idx not in words_by_idx:
        return

    # Here we loop through the dictionary to find a valid substring
    for word in words_by_idx[idx]:
        # We make sure the substring(or all counts or the substring) is not used
        if words_count[word] > 0:
            # Add the substring to a possible solution
            used_words.append(word)
            # And remove from the words_count, so we don't use it more times than allowed
            words_count[word] -= 1
            # We call the same function and increase the index by the length of the substring, so we can search for the
            # next one. If the length of found combination is the same as target's, this means we have found a solution
            # We go to line 43 and print
            findallsolutions(idx + len(word), target, words_by_idx, words_count, used_words)
            # If we are here it means that idx not in words_by_idx, so we remove all unusable
            # substrings starting from the end (the backtracking)
            used_words.pop()
            # And we return the substring into the words count, so we can use it again
            words_count[word] += 1


findallsolutions(0, target, words_by_idx,  words_count, [])

