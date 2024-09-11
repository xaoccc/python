import pandas as pd
def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return person.loc[person.email.duplicated(), ['email']].drop_duplicates().rename(columns={'email': 'Email'})