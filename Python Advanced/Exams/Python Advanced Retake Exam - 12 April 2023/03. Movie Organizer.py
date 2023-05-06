def movie_organizer(*movies):
    movies_collection = {}
    result = ""
    for i in range(len(movies)):
        if movies[i][1] not in movies_collection:
            movies_collection[movies[i][1]] = [movies[i][0]]
        else:
            movies_collection[movies[i][1]].append(movies[i][0])
    movies_collection = dict(sorted(movies_collection.items(), key=lambda x: (-len(x[1]), x[0])))  
    for genre, movie in movies_collection.items():
        movie.sort()
        movies_collection[genre] = movie
        result += f"{genre} - {len(movie)}\n"
        for i in movie:
            result += f"* {i}\n"
        
    return result
