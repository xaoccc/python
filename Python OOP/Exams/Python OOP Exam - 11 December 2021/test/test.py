from project.team import Team
import unittest

class TestTeam(unittest.TestCase):
    def setUp(self) -> None:
        self.team = Team("Levski")

    def test_init(self):
        self.assertEqual("Levski", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_not_alpha(self):
        with self.assertRaises(ValueError) as valer:
            self.team.name = "Bor4e"
        self.assertEqual("Team Name can contain only letters!", str(valer.exception))
        self.assertEqual("Levski", self.team.name)

    def test_add_member(self):
        self.assertEqual("Successfully added: Pesho, Ivan, Stamat", self.team.add_member(Pesho=17, Ivan=32, Stamat=18))
        self.assertEqual({"Pesho": 17, "Ivan": 32, "Stamat": 18}, self.team.members)
        self.assertEqual("Successfully added: Gosho", self.team.add_member(Pesho=22, Gosho=24))
        self.assertEqual({"Pesho": 17, "Ivan": 32, "Stamat": 18, "Gosho": 24}, self.team.members)

    def test_remove_member(self):
        self.team.add_member(Pesho=17, Ivan=32, Stamat=18)
        self.assertEqual("Member Pesho removed", self.team.remove_member("Pesho"))
        self.assertEqual({"Ivan": 32, "Stamat": 18}, self.team.members)
        self.assertEqual("Member with name Stanko does not exist", self.team.remove_member("Stanko"))
        self.assertEqual({"Ivan": 32, "Stamat": 18}, self.team.members)

    def test__len__(self):
        self.team.add_member(Pesho=17, Ivan=32, Stamat=18)
        self.assertEqual(3, len(self.team))

    def test__gt__(self):
        self.team.add_member(Pesho=17, Ivan=32, Stamat=18)
        other_team = Team("Ceseka")
        other_team.add_member(Canko=17, Vanko=32)
        self.assertEqual(True, self.team.__gt__(other_team))
        self.assertEqual(False, other_team.__gt__(self.team))
        other_team.add_member(Canko=17, Vanko=32, Nacko=16, Yanko=23)
        self.assertEqual(False, self.team.__gt__(other_team))
        self.assertEqual(True, other_team.__gt__(self.team))

    def test__add__(self):
        self.team.add_member(Pesho=17, Ivan=32, Stamat=18)
        other_team = Team("Ceseka")
        other_team.add_member(Canko=17, Vanko=32)
        self.team.__add__(other_team)
        self.assertEqual("LevskiCeseka", self.team.__add__(other_team).name)
        self.assertEqual({"Pesho": 17, "Ivan": 32, "Stamat": 18, "Canko": 17, "Vanko": 32}, self.team.__add__(other_team).members)

    def test__str__no_members(self):
        self.assertEqual("Team name: Levski", str(self.team))

    def test__str__with_members(self):
        self.team.add_member(Pesho=17, Ivan=32, Stamat=18)
        self.assertEqual("Team name: Levski\nMember: Ivan - 32-years old\n"
                         "Member: Stamat - 18-years old\n"
                         "Member: Pesho - 17-years old", str(self.team))


if __name__ == "__main__":
    unittest.main()
