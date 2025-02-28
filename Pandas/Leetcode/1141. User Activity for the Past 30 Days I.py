import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    activity_filtered = activity.loc[(activity["activity_date"] > "2019-06-27") & (activity["activity_date"] <= "2019-07-27"), : ].rename(columns={"activity_date": "day", "user_id": "active_users"}).drop_duplicates(subset=["active_users", "day"]).groupby(by=['day'], as_index=False).count()

    return activity_filtered[["day", "active_users"]]