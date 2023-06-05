def positive_index(idx):
    if idx > 0:
        return idx
    return positive_index(idx + array_length)
