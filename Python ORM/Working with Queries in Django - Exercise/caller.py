import os
import django
from django.db.models import Q

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal, Dungeon, Workout


# Import your models
# Create and check models
# Run and print your queries


def show_highest_rated_art():
    best_art = ArtworkGallery.objects.all().order_by("-rating", "id").first()
    return f"{best_art.art_name} is the highest-rated art with a {best_art.rating} rating!"


def bulk_create_arts(first_art, second_art):
    ArtworkGallery.objects.bulk_create([first_art, second_art])

def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()


def show_the_most_expensive_laptop():
    top_laptop = Laptop.objects.order_by("-price", "-id").first()
    return f"{top_laptop.brand} is the most expensive laptop available for {top_laptop.price}$!"



def bulk_create_laptops(*args):
    Laptop.objects.bulk_create(*args)


def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=["Asus", "Lenovo"]).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=["Apple", "Dell", "Acer"]).update(memory=16)


def update_operation_systems():
    Laptop.objects.filter(brand="Asus").update(operation_system="Windows")
    Laptop.objects.filter(brand="Apple").update(operation_system="MacOS")
    Laptop.objects.filter(brand__in=["Dell", "Acer"]).update(operation_system="Linux")
    Laptop.objects.filter(brand="Lenovo").update(operation_system="Chrome OS")

def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()


def bulk_create_chess_players(*args):
    ChessPlayer.objects.bulk_create(*args)

def delete_chess_players():
    ChessPlayer.objects.filter(title="no title").delete()

def change_chess_games_won():
    ChessPlayer.objects.filter(title="GM").update(games_won=30)

def change_chess_games_lost():
    ChessPlayer.objects.filter(title="no title").update(games_lost=25)

def change_chess_games_drawn():
    ChessPlayer.objects.all().update(games_drawn=10)

def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title="GM")

def grand_chess_title_IM():
    ChessPlayer.objects.filter(Q(rating__gte=2300) & Q(rating__lt=2400)).update(title="IM")

def grand_chess_title_FM():
    ChessPlayer.objects.filter(Q(rating__gte=2200) & Q(rating__lt=2300)).update(title="FM")

def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating__lt=2200).update(title="regular player")

# Create two instances of ChessPlayer

# player1 = ChessPlayer(
#     username='Player1',
#     title='no title',
#     rating=2200,
#     games_played=50,
#     games_won=20,
#     games_lost=25,
#     games_drawn=5,
# )
#
# player2 = ChessPlayer(
#     username='Player2',
#     title='IM',
#     rating=2350,
#     games_played=80,
#     games_won=40,
#     games_lost=25,
#     games_drawn=15
# )

# Test code:
# bulk_create_chess_players([player1, player2])
# delete_chess_players()
# change_chess_games_won()
# change_chess_games_lost()
# change_chess_games_drawn()
# grand_chess_title_GM()
# grand_chess_title_IM()
# grand_chess_title_FM()
# grand_chess_title_regular_player()

def set_new_chefs():
    Meal.objects.filter(meal_type="Breakfast").update(chef="Gordon Ramsay")
    Meal.objects.filter(meal_type="Lunch").update(chef="Julia Child")
    Meal.objects.filter(meal_type="Dinner").update(chef="Jamie Oliver")
    Meal.objects.filter(meal_type="Snack").update(chef="Thomas Keller")


def set_new_preparation_times():
    Meal.objects.filter(meal_type="Breakfast").update(preparation_time="10 minutes")
    Meal.objects.filter(meal_type="Lunch").update(preparation_time="12 minutes")
    Meal.objects.filter(meal_type="Dinner").update(preparation_time="15 minutes")
    Meal.objects.filter(meal_type="Snack").update(preparation_time="5 minutes")

def update_low_calorie_meals():
    Meal.objects.filter(Q(meal_type="Breakfast") | Q(meal_type="Dinner")).update(calories=400)

def update_high_calorie_meals():
    Meal.objects.filter(Q(meal_type="Lunch") | Q(meal_type="Snack")).update(calories=700)

def delete_lunch_and_snack_meals():
    Meal.objects.filter(Q(meal_type="Lunch") | Q(meal_type="Snack")).delete()

# meal1 = Meal.objects.create(
#     name="Pancakes",
#     meal_type="Breakfast",
#     preparation_time="20 minutes",
#     difficulty=3,
#     calories=350,
#     chef="Jane",
# )
#
# meal2 = Meal.objects.create(
#     name="Spaghetti Bolognese",
#     meal_type="Dinner",
#     preparation_time="45 minutes",
#     difficulty=4,
#     calories=550,
#     chef="Sarah",
# )


# Test code
# set_new_chefs()
# set_new_preparation_times()
# update_low_calorie_meals()
# update_high_calorie_meals()
# delete_lunch_and_snack_meals()

def bulk_create_dungeons(*args):
    Dungeon.objects.bulk_create(*args)


def show_hard_dungeons():
    dungeons = Dungeon.objects.filter(difficulty="Hard").order_by("-location")
    result = []
    for d in dungeons:
        result.append(f"{d.name} is guarded by {d.boss_name} who has {d.boss_health} health points!")
    return "\n".join(result)


def update_dungeon_names():
    Dungeon.objects.filter(difficulty="Easy").update(name="The Erased Thombs")
    Dungeon.objects.filter(difficulty="Medium").update(name="The Coral Labyrinth")
    Dungeon.objects.filter(difficulty="Hard").update(name="The Lost Haunt")

def update_dungeon_bosses_health():
    Dungeon.objects.exclude(difficulty="Easy").update(boss_health=500)

def update_dungeon_recommended_levels():
    Dungeon.objects.filter(difficulty="Easy").update(recommended_level=25)
    Dungeon.objects.filter(difficulty="Medium").update(recommended_level=50)
    Dungeon.objects.filter(difficulty="Hard").update(recommended_level=75)


def update_dungeon_rewards():
    Dungeon.objects.filter(boss_health=500).update(reward="1000 Gold")
    Dungeon.objects.filter(location__startswith="E").update(reward="New dungeon unlocked")
    Dungeon.objects.filter(location__endswith="s").update(reward="Dragonheart Amulet")

def set_new_locations():
    Dungeon.objects.filter(recommended_level=25).update(location="Enchanted Maze")
    Dungeon.objects.filter(recommended_level=50).update(location="Grimstone Mines")
    Dungeon.objects.filter(recommended_level=75).update(location="Shadowed Abyss")

dungeon1 = Dungeon(
    name="Dungeon 1",
    boss_name="Boss 1",
    boss_health=1000,
    recommended_level=75,
    reward="Gold",
    location="Eternal Hell",
    difficulty="Hard",
)

dungeon2 = Dungeon(
    name="Dungeon 2",
    boss_name="Boss 2",
    boss_health=500,
    recommended_level=25,
    reward="Experience",
    location="Crystal Caverns",
    difficulty="Easy",
)

# Test code:
# bulk_create_dungeons([dungeon1, dungeon2])
# print(show_hard_dungeons())
# update_dungeon_names()
# update_dungeon_bosses_health()
# update_dungeon_recommended_levels()
# update_dungeon_rewards()
# set_new_locations()

def show_workouts():
    workouts = Workout.objects.filter(Q(workout_type="Calisthenics") | Q(workout_type="CrossFit"))
    result = []
    for w in workouts:
        result.append(f"{w.name} from {w.workout_type} type has {w.difficulty} difficulty!")
    return "\n".join(result)

def get_high_difficulty_cardio_workouts():
    return  Workout.objects.filter(Q(workout_type="Cardio") & Q(difficulty="High")).order_by("instructor")

def set_new_instructors():
    Workout.objects.filter(workout_type="Cardio").update(instructor="John Smith")
    Workout.objects.filter(workout_type="Strength").update(instructor="Michael Williams")
    Workout.objects.filter(workout_type="Yoga").update(instructor="Emily Johnson")
    Workout.objects.filter(workout_type="CrossFit").update(instructor="Sarah Davis")
    Workout.objects.filter(workout_type="Calisthenics").update(instructor="Chris Heria")

def set_new_duration_times():
    Workout.objects.filter(instructor="John Smith").update(duration="15 minutes")
    Workout.objects.filter(instructor="Sarah Davis").update(duration="30 minutes")
    Workout.objects.filter(instructor="Chris Heria").update(duration="45 minutes")
    Workout.objects.filter(instructor="Michael Williams").update(duration="1 hour")
    Workout.objects.filter(instructor="Emily Johnson").update(duration="1 hour and 30 minutes")

def delete_workouts():
    Workout.objects.exclude(workout_type__in=["Strength", "Calisthenics"]).delete()

# Test code:
# workout1 = Workout.objects.create(
#     name="Push-Ups",
#     workout_type="Calisthenics",
#     duration="10 minutes",
#     difficulty="Intermediate",
#     calories_burned=200,
#     instructor="Chris Heria"
# )
#
# workout2 = Workout.objects.create(
#     name="Running",
#     workout_type="Cardio",
#     duration="30 minutes",
#     difficulty="High",
#     calories_burned=400,
#     instructor="John Smith"
# )
# print(show_workouts())
# high_difficulty_cardio_workouts = get_high_difficulty_cardio_workouts()
# for workout in high_difficulty_cardio_workouts:
#     print(f"{workout.name} by {workout.instructor}")

# set_new_instructors()
# set_new_duration_times()
# delete_workouts()