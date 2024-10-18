def dropMissingData(students):
    return students.dropna(how='any', subset='name')