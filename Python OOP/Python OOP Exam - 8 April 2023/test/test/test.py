from project.tennis_player import TennisPlayer
import unittest


class TennisPlayerTests(unittest.TestCase):
    def setUp(self):
        self.player = TennisPlayer("Grisho", 28, 215)

    def test_init(self):
        self.assertEqual("Grisho", self.player.name)
        self.assertEqual(28, self.player.age)
        self.assertEqual(215, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_blank(self):
        with self.assertRaises(ValueError) as val:
            self.player.name = ""
        self.assertEqual("Name should be more than 2 symbols!", str(val.exception))
        self.assertEqual("Grisho", self.player.name)

    def test_name_two_chars(self):
        with self.assertRaises(ValueError) as val:
            self.player.name = "BG"
        self.assertEqual("Name should be more than 2 symbols!", str(val.exception))
        self.assertEqual("Grisho", self.player.name)

    def test_age(self):
        with self.assertRaises(ValueError) as val:
            self.player.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(val.exception))
        self.assertEqual(28, self.player.age)

    def test_add_new_win(self):
        self.player.add_new_win("Grand open Kozlodui")
        self.assertEqual(["Grand open Kozlodui"], self.player.wins)
        self.assertEqual("Grand open Kozlodui has been already added to the list of wins!",
                         self.player.add_new_win("Grand open Kozlodui"))
        self.assertEqual(["Grand open Kozlodui"], self.player.wins)

    def test_if_player_points_smaller_than_other_player(self):
        other = TennisPlayer("Nadal", 28, 315)
        self.assertEqual('Nadal is a top seeded player and he/she is better than Grisho', self.player.__lt__(other))

    def test_if_player_points_larger_than_other_player(self):
        other = TennisPlayer("Nadal", 28, 50)
        self.assertEqual('Grisho is a better player than Nadal', self.player.__lt__(other))

    def test_player_info_print(self):
        self.player.add_new_win("Grand open Kozlodui")
        self.player.add_new_win("Grand open Lukovit")
        self.assertEqual("Tennis Player: Grisho\nAge: 28\nPoints: 215.0\nTournaments won: Grand open Kozlodui, Grand open Lukovit", str(self.player))


if __name__ == "__main__":
    unittest.main()
