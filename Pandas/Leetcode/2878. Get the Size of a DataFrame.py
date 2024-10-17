def getDataframeSize(players):
    cols = players.count().count()
    return [int(players.size / cols), int(cols)]