def renameColumns(students):
    return students.rename(
        columns={'id': 'student_id', 'first': 'first_name', 'last': 'last_name', 'age': 'age_in_years'})
