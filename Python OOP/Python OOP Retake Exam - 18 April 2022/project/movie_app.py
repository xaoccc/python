from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.thriller import Thriller
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    @staticmethod
    def find_user(users, username):
        for user in users:
            if user.username == username:
                return user

    def register_user(self, username: str, age: int):
        if self.find_user(self.users_collection, username):
            raise Exception("User already exists!")

        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):

        if not self.find_user(self.users_collection, username):
            raise Exception("This user does not exist!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        current_user = self.find_user(self.users_collection, username)

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        current_user.movies_owned.append(movie)
        movie.owner = current_user
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")


        for movie_attribute, new_attribute_value in kwargs.items():
            if movie_attribute == "title":
                movie.title = new_attribute_value
            elif movie_attribute == "year":
                movie.year = new_attribute_value
            elif movie_attribute == "age_restriction":
                movie.age_restriction = new_attribute_value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        current_user = self.find_user(self.users_collection, username)

        current_user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        if username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        current_user = self.find_user(self.users_collection, username)
        if movie in current_user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        current_user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        current_user = self.find_user(self.users_collection, username)
        if movie not in current_user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie.likes -= 1
        current_user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        movies_dict = {}
        for movie in self.movies_collection:
            movies_dict[movie] = [movie.year, movie.title]

        movies_dict = dict(sorted(movies_dict.items(), key=lambda x: (-x[1][0], x[1][1])))
        result = []
        for m in movies_dict.keys():
            result.append(m.details())
        return "\n".join(result)

    def __str__(self):
        if self.users_collection:
            result = "All users: "
            for u in self.users_collection:
                result += f"{u.username}, "
            result = result[:-2]
        else:
            result = "All users: No users."

        if self.movies_collection:
            result += "\nAll movies: "
            for m in self.movies_collection:
                result += f"{m.title}, "
            result = result[:-2]
        else:
            result += "\nAll movies: No movies."
        return result


# movie_app = MovieApp()
# print(movie_app.register_user('Martin', 24))
# user = movie_app.users_collection[0]
# movie = Action('Die Hard', 1988, user, 18)
# print(movie_app.upload_movie('Martin', movie))
# print(movie_app.movies_collection[0].title)
# print(movie_app.register_user('Alexandra', 25))
# user2 = movie_app.users_collection[1]
# movie2 = Action('Free Guy', 2021, user2, 16)
# print(movie_app.upload_movie('Alexandra', movie2))
#
# print(movie_app.edit_movie('Alexandra', movie2, title="Free Guy 2"))
# print(movie_app.edit_movie('Alexandra', movie2, title="Free Guy 3"))
# print(movie_app.edit_movie('Alexandra', movie2, title="Free Guy 4"))
#
# print(movie_app.like_movie('Martin', movie2))
# print(movie_app.edit_movie('Martin', movie2, title="Die Hard", ))


# print(movie_app.like_movie('Alexandra', movie))
# print(movie_app.dislike_movie('Martin', movie2))
# print(movie_app.like_movie('Martin', movie2))
# print(movie_app.delete_movie('Alexandra', movie2))
# movie2 = Fantasy('The Lord of the Rings', 2023, user2, 14)
# print(movie_app.upload_movie('Alexandra', movie2))
# print(movie_app.display_movies())
# print(movie_app)



