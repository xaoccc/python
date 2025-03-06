import pandas as pd


def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by=['machine_id', 'process_id', 'activity_type'], ascending=[True, True, False], inplace=True)
    activity['processing_time'] = activity.groupby(['machine_id', 'process_id'])['timestamp'].diff().fillna(0)
    filtered = activity[['machine_id', 'process_id', 'processing_time']].groupby(by=['machine_id', 'process_id'],
                                                                                 as_index=False).sum()[
        ['machine_id', 'process_id', 'processing_time']]
    return filtered[['machine_id', 'processing_time']].groupby(by=['machine_id'], as_index=False).mean()[
        ['machine_id', 'processing_time']].round(3)
