import pandas as pd

def article_views(views):
    return views.loc[(views['author_id'] == views['viewer_id']), ['author_id']].rename(columns={'author_id': 'id'}).drop_duplicates().sort_values(by='id')