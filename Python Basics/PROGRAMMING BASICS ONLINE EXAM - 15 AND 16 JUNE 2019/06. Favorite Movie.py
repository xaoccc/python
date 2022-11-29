movie_name = ""
movie_num = 0
max_movie_pts = 0
best_movie = ""
movie_pts = 0

while True:
    movie_name = input()
    if movie_name == "STOP":
        break
    movie_num += 1
    if movie_num == 7:
        print("The limit is reached.")
        break
 
    movie_pts = 0
    for i in range(len(movie_name)):
        movie_pts += ord(movie_name[i])
        if 96 < ord(movie_name[i]) < 123:
            movie_pts -= 2 * len(movie_name)
        if 64 < ord(movie_name[i]) < 91:
            movie_pts -= len(movie_name)
    if movie_pts > max_movie_pts:
        max_movie_pts = movie_pts
        best_movie = movie_name
        
print(f"The best movie for you is {best_movie} with {max_movie_pts} ASCII sum.")
