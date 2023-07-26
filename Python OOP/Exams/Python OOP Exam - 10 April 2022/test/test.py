from project.movie import Movie
import unittest


class TestMovie(unittest.TestCase):
    def setUp(self) -> None:
        self.movie = Movie("The Conjuring", 2013, 7.5)

    def test_init(self):
        self.assertEqual("The Conjuring", self.movie.name)
        self.assertEqual(2013, self.movie.year)
        self.assertEqual(7.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_empty_string(self):
        with self.assertRaises(ValueError) as valer:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(valer.exception))

    def test_year_invalid_year(self):
        with self.assertRaises(ValueError) as valer:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!", str(valer.exception))

    def test_add_actor(self):
        self.movie.actors = ["Patrick Wilson", "Vera Fermiga"]
        self.assertEqual("Patrick Wilson is already added in the list of actors!", self.movie.add_actor("Patrick Wilson"))
        self.assertEqual(["Patrick Wilson", "Vera Fermiga"], self.movie.actors)
        self.movie.add_actor("Jack Nicholson")
        self.assertEqual(["Patrick Wilson", "Vera Fermiga", "Jack Nicholson"], self.movie.actors)

    def test_better_movie_self(self):
        movie_two = Movie("It", 1990, 7)
        self.assertEqual('"The Conjuring" is better than "It"',
                         self.movie.__gt__(movie_two))

    def test_better_movie_other(self):
        movie_two = Movie("Constantine", 1990, 7.7)
        self.assertEqual('"Constantine" is better than "The Conjuring"',
                         self.movie.__gt__(movie_two))

    def test__repr__no_actors(self):
        self.assertEqual(f"Name: The Conjuring\n" 
               f"Year of Release: 2013\n" 
               f"Rating: 7.50\n" 
               f"Cast: ", str(self.movie))

    def test__repr__actors(self):
        self.movie.actors = ["Patrick Wilson", "Vera Fermiga"]
        self.assertEqual(f"Name: The Conjuring\n" 
               f"Year of Release: 2013\n" 
               f"Rating: 7.50\n" 
               f"Cast: Patrick Wilson, Vera Fermiga", str(self.movie))