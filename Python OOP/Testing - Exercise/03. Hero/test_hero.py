import unittest
from project.hero import Hero


class HeroTests(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("GotinPich93", 26, 1500, 35)
        self.enemy_hero_same_name = Hero("GotinPich93", 26, 150, 35)
        self.enemy_hero = Hero("Ivan", 16, 1000, 30)
        self.enemy_hero_no_hp = Hero("Slabak", 26, 0, 35)
        self.enemy_hero_winner = Hero("Ivan", 88, 5000, 108)
    
    def test_name(self):
        result = self.hero.username 
        expected_result = "GotinPich93"
        self.assertEqual(result, expected_result)
        
    def test_level(self):
        result = self.hero.level
        expected_result = 26
        self.assertEqual(result, expected_result)
        
    def test_health(self):
        result = self.hero.health
        expected_result = 1500
        self.assertEqual(result, expected_result)
        
    def test_damage(self):
        result = self.hero.damage 
        expected_result = 35
        self.assertEqual(result, expected_result)
        
    def test_battle_self(self):
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.enemy_hero_same_name)
        self.assertEqual("You cannot fight yourself", str(context.exception))
        
    def test_battle_low_hp_self(self):
        with self.assertRaises(Exception) as context:
            self.hero = Hero("GotinPich93", 26, 0, 35)
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))
        
    def test_battle_low_hp_enemy(self):
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.enemy_hero_no_hp)
        self.assertEqual("You cannot fight Slabak. He needs to rest", str(context.exception))
        
    def test_battle_ok_self_hp(self):
        self.hero.battle(self.enemy_hero)
        result = self.hero.health
        expected_result = 1020
        self.assertEqual(result, expected_result)
        
    def test_battle_ok_emeny_hp(self):
        self.hero.battle(self.enemy_hero)
        result = self.enemy_hero.health
        expected_result = 95
        self.assertEqual(result, expected_result)
        
    def test_battle_draw(self):
        self.hero = Hero("GotinPich93", 26, 300, 30)
        self.enemy_hero = Hero("Ivan", 16, 500, 30)
        self.assertEqual("Draw", self.hero.battle(self.enemy_hero))
        
    def test_battle_enemy_dead_self_level(self):
        self.enemy_hero = Hero("Ivan", 16, 500, 30)
        self.hero.battle(self.enemy_hero)
        result = self.hero.level
        expected_result = 27
        self.assertEqual(result, expected_result)
    
    def test_battle_enemy_dead_self_damage(self):
        self.enemy_hero = Hero("Ivan", 16, 500, 30)
        self.hero.battle(self.enemy_hero)
        result = self.hero.damage
        expected_result = 40
        self.assertEqual(result, expected_result)
        
    def test_battle_enemy_dead_self_health(self):
        self.enemy_hero = Hero("Ivan", 16, 500, 30)
        self.hero.battle(self.enemy_hero)
        result = self.hero.health
        expected_result = 1025
        self.assertEqual(result, expected_result)
        
    def test_battle_enemy_dead_self_win(self):
        self.enemy_hero = Hero("Ivan", 16, 500, 30)
        self.assertEqual("You win", self.hero.battle(self.enemy_hero))
        
    def test_battle_enemy_win_level(self):
        self.hero.battle(self.enemy_hero_winner)
        result = self.enemy_hero_winner.level
        expected_result = 89
        self.assertEqual(result, expected_result)
    
    def test_battle_enemy_win_damage(self):
        self.hero.battle(self.enemy_hero_winner)
        result = self.enemy_hero_winner.damage
        expected_result = 113
        self.assertEqual(result, expected_result)
        
    def test_battle_enemy_win_health(self):
        self.hero.battle(self.enemy_hero_winner)
        result = self.enemy_hero_winner.health
        expected_result = 4095
        self.assertEqual(result, expected_result)
        
    def test_battle_enemy_win(self):
        self.assertEqual("You lose", self.hero.battle(self.enemy_hero_winner))
        
    def test_str(self):
        self.assertEqual("Hero GotinPich93: 26 lvl\nHealth: 1500\nDamage: 35\n", str(self.hero))

if __name__ == "__main__":
    unittest.main()