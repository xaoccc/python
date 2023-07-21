from project.truck_driver import TruckDriver
import unittest


class TestTruckDriver(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("Trifon", 1.28)

    def test_init(self):
        self.assertEqual(self.driver.name, "Trifon")
        self.assertEqual(self.driver.money_per_mile, 1.28)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    def test_earned_money_negative(self):
        with self.assertRaises(ValueError) as valer:
            self.driver.earned_money = -1
        self.assertEqual("Trifon went bankrupt.", str(valer.exception))

    def test_add_cargo_offer_already_added(self):
        self.driver.available_cargos = {"HMMC": 1700}
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("HMMC", 1700)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_add_new_offer(self):
        self.assertEqual("Cargo for 1700 to HMMC was added as an offer.", self.driver.add_cargo_offer("HMMC", 1700))
        self.assertEqual({"HMMC": 1700}, self.driver.available_cargos)

    def test_best_cargo_offer_no_offers(self):
        self.assertEqual("There are no offers available.", self.driver.drive_best_cargo_offer())

    def test_best_cargo_offer_offers(self):
        self.driver.available_cargos = {"HMMC": 1700, "Valencia": 4600, "Varna": 470}
        self.assertEqual("Trifon is driving 4600 to Valencia.", self.driver.drive_best_cargo_offer())
        self.assertEqual(3848.0, self.driver.earned_money)
        self.assertEqual(4600.0, self.driver.miles)
        # self.assertEqual(3848.0, self.driver.check_for_activities(4600))

    def test_eat(self):
        self.driver.earned_money = 1000
        self.driver.eat(1000)
        self.assertEqual(980, self.driver.earned_money)
        self.driver.eat(360)
        self.assertEqual(980, self.driver.earned_money)

    def test_sleep(self):
        self.driver.earned_money = 1000
        self.driver.sleep(1000)
        self.assertEqual(955, self.driver.earned_money)
        self.driver.sleep(360)
        self.assertEqual(955, self.driver.earned_money)

    def test_pump_gas(self):
        self.driver.earned_money = 3600
        self.driver.pump_gas(1500)
        self.assertEqual(3100, self.driver.earned_money)
        self.driver.pump_gas(360)
        self.assertEqual(3100, self.driver.earned_money)

    def test_repair_truck(self):
        self.driver.earned_money = 8500
        self.driver.repair_truck(20000)
        self.assertEqual(1000, self.driver.earned_money)
        self.driver.repair_truck(360)
        self.assertEqual(1000, self.driver.earned_money)

    def test_check_for_activities(self):
        self.driver.earned_money = 22000
        self.driver.check_for_activities(11000)
        self.assertEqual(9625, self.driver.earned_money)

    def test_repr(self):
        self.driver.available_cargos = {"HMMC": 1700, "Valencia": 4600, "Varna": 470}
        self.driver.drive_best_cargo_offer()
        self.assertEqual("Trifon has 4600 miles behind his back.", str(self.driver))


if __name__ == "__main__":
    unittest.main()