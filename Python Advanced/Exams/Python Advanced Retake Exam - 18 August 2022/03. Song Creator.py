def add_songs(*args):
    songs = {}
    sing = ""
    for song in args:

        if song[0] not in songs:
            songs[song[0]] = song[1]
        else:
            songs[song[0]] += song[1]
    for song, text in songs.items():
        sing += f"- {song}\n"
        if text:
            text = '\n'.join(text)
            sing += f"{text}\n"
    return sing
