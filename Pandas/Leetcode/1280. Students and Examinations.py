import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame,
                              examinations: pd.DataFrame) -> pd.DataFrame:
    # Create df1: examination_count, where we have columns: 'student_id', 'subject_name' and 'attended_exams'
    examination_count = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')

    # Create df2: CROSS JOIN between students and subjects, so we can have all combinations of [student,subject]
    student_subject = pd.merge(students, subjects, how='cross')

    result_df = student_subject.merge(examination_count, on=['student_id', 'subject_name'], how='left')

    return result_df.sort_values(['student_id', 'subject_name']).replace({'attended_exams': np.nan}, 0)