import os
import django
from _decimal import Decimal
from django.db.models import Q, Count, Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# Create and run your queries within functions
from main_app.models import Director, Actor, Movie


# Create your tests here.
def get_directors(search_name=None, search_nationality=None):
    result = []

    if not search_name:
        search_name = "%%%"

    if not search_nationality:
        search_nationality = "%%%"

    # elif search_nationality and search_name:
    found_directors = Director.objects.filter(Q(full_name__icontains=search_name) | Q(nationality__icontains=search_nationality)).order_by("full_name")
    for director in found_directors:
        result.append(f"Director: {director.full_name}, nationality: {director.nationality}, experience: {director.years_of_experience}")
    return "\n".join(result)

def get_top_director():
    top_director = Director.objects.get_directors_by_movies_count().first()
    if top_director.exists():
        return f"Top Director: {top_director.full_name}, movies: {top_director.movies_num}."
    return ""

def get_top_actor():
    top_actor = Actor.objects.prefetch_related("movie_set").annotate(movies_num=Count("movie")).order_by("-movies_num", "full_name").first()
    if not top_actor.exists() or not top_actor.movies_num:
        return ""

    movies = top_actor._prefetched_objects_cache["movie_set"]

    average_rating = movies.aggregate(Avg("rating"))["rating__avg"]
    movies_titles = []
    for movie in movies:
        movies_titles.append(movie.title)

    return f"Top Actor: {top_actor.full_name}, starring in movies: {', '.join(movies_titles)}, movies average rating: {average_rating:.1f}"

def get_actors_by_movies_count():
    top_actors = Actor.objects.annotate(movies_num=Count("actors")).order_by("-movies_num", "full_name").filter(movies_num__gt=0)[:3]

    if not top_actors:
        return ""

    result = []
    for actor in top_actors:
        result.append(f"{actor.full_name}, participated in {actor.movies_num} movies")
    return "\n".join(result)

def get_top_rated_awarded_movie():
    top_movie = Movie.objects.select_related('starring_actor').prefetch_related("actors").filter(is_awarded=True).order_by("-rating", "title").first()
    if top_movie is None:
        return ""

    starring_actor = top_movie.starring_actor.full_name if top_movie.starring_actor else "N/A"
    cast = []
    for actor in top_movie._prefetched_objects_cache["actors"]:
        cast.append(actor.full_name)
    return f"Top rated awarded movie: {top_movie.title}, rating: {top_movie.rating:.1f}. Starring actor: {starring_actor}. Cast: {', '.join(cast)}."

def increase_rating():
    classic_movies = Movie.objects.filter(is_classic=True, rating__lte=9.9)

    if classic_movies.exists():
        classic_movies.update(rating=F("rating") + 0.1)
        return f"Rating increased for {classic_movies.count()} movies."

    return "No ratings increased."

# print(get_directors(search_name=None, search_nationality="B"))
# print(get_top_director())
# print(get_top_actor())

# print(get_actors_by_movies_count())
# print(get_top_rated_awarded_movie())
# print(increase_rating())


# access every RELATED object in the prefetch related table:
all_movies = Movie.objects.all()

# If we look at the first Movie object, we can see that, we can access directly the ForeignKey objects Actor and Director,
# but we cannot access directly the ManyToMany objects Actors!
first_movie_details = Movie.objects.first().__dict__
print(first_movie_details)
print(Movie.objects.first().starring_actor.full_name)

all_movies_with_their_actors = Movie.objects.prefetch_related("actors")

for movie in all_movies_with_their_actors:
    # Here we can select all() actors,
    current_movie_actors = movie.actors.all()
    # or we can filter() them
    # Using Filter we can:
    # 1. See all movies an actor is participating, searcing by full name
    current_movie_actors = movie.actors.filter(full_name="Stefan Danailov")

    # or by id
    current_movie_actors = movie.actors.filter(id=1)

    # 2. See movies with youngest/oldest actors
    current_movie_actors = movie.actors.filter(birth_date__gte="1970-01-01")

    # 3. Search actors and movies by actor name or part of the name
    current_movie_actors = movie.actors.filter(full_name__contains="test")

    # and much, much more: order, update, delete, etc...
    if current_movie_actors:
        print(f"Movie {movie.title, movie.release_date} cast:")
        # create, update, delete:
        # current_movie_actors.update(full_name="test test")
        # current_movie_actors.delete()
        # current_movie_actors.create(id=1, full_name="Stefan Danailov", birth_date="1942-12-09", nationality="Bulgarian", is_awarded=True, last_updated="1998-05-05")
        for actor in current_movie_actors:
            print(actor.id, actor.full_name)


# We can do the reverse search and find all movies from Actor model:
all_actors_with_their_movies = Actor.objects.prefetch_related("movie_set")
print(all_actors_with_their_movies)

for actor in all_actors_with_their_movies:
    current_actor_movies = actor.movie_set.all()
    if current_actor_movies:
        print(f"Actor {actor.full_name} is playing in the following movies:")
        for movie in current_actor_movies:
            print(f"{movie.title, movie.release_date}")