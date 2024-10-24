import pandas as pd


def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    new_data = pd.Series([])
    student = seat['student']
    rows = student.size
    for i in range(rows):
        if i % 2 == 0:
            if i + 1 < rows:
                new_data[i] = student[i + 1]
            else:
                new_data[i] = student[i]
        else:
            new_data[i] = student[i - 1]
    seat['student'] = new_data
    return seat
