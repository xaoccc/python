from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.drink.tea import Tea
from project.drink.water import Water
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake


class Bakery:
    food_types = {"Bread": Bread, "Cake": Cake}
    drink_types = {"Tea": Tea, "Water": Water}
    table_types = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @staticmethod
    def find_food(food_name, food_menu):
        for food in food_menu:
            if food.name == food_name:
                return food

    @staticmethod
    def find_drink(drink_name, drinks_menu):
        for drink in drinks_menu:
            if drink.name == drink_name:
                return drink

    @staticmethod
    def find_table(table_number, tables):
        for table in tables:
            if table.table_number == table_number:
                return table

    def add_food(self, food_type: str, name: str, price: float):
        if self.find_food(name, self.food_menu):
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type in self.food_types:
            self.food_menu.append(self.food_types[food_type](name, price))
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if self.find_drink(name, self.drinks_menu):
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in self.drink_types:
            self.drinks_menu.append((self.drink_types[drink_type](name, portion, brand)))
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if self.find_table(table_number, self.tables_repository):
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in self.table_types:
            self.tables_repository.append(self.table_types[table_type](table_number, capacity))
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        current_table = self.find_table(table_number, self.tables_repository)

        if not current_table:
            return f"Could not find table {table_number}"

        current_order = [f"Table {table_number} ordered:"]
        not_in_menu = [f"{self.name} does not have in the menu:"]
        for food in food_names:
            current_food = self.find_food(food, self.food_menu)
            if current_food:
                current_table.order_food(current_food)
                current_order.append(str(current_food))
            else:
                not_in_menu.append(food)
        result = current_order + not_in_menu
        return "\n".join(result)

    def order_drink(self, table_number: int, *drinks_names):
        current_table = self.find_table(table_number, self.tables_repository)

        if not current_table:
            return f"Could not find table {table_number}"

        current_order = [f"Table {table_number} ordered:"]
        not_in_menu = [f"{self.name} does not have in the menu:"]
        for drink in drinks_names:
            current_drink = self.find_drink(drink, self.drinks_menu)
            if current_drink:
                current_table.order_drink(current_drink)
                current_order.append(str(current_drink))
            else:
                not_in_menu.append(drink)
        result = current_order + not_in_menu
        return "\n".join(result)

    def leave_table(self, table_number: int):
        table = self.find_table(table_number, self.tables_repository)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        result = []
        for table in self.tables_repository:
            result.append(table.free_table_info())
        return "\n".join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"


# bakery = Bakery("Sunny")
#
# print(f"\n\n{'# ADD_FOOD'}")
# print(bakery.add_food("Bread", "Sour", 1.50))
# print(bakery.add_food("Bread", "White", 1.30))
# print(bakery.add_food("Cake", "Chocolate", 2.90))
# print(bakery.add_food("Cake", "Vanilla", 2.90))
#
# print(f"\n\n{'# ADD_DRINK'}")
# print(bakery.add_drink("Water", "Spring", 250, "Bankya"))
# print(bakery.add_drink("Water", "Mineral", 500, "Devin"))
# print(bakery.add_drink("Tea", "Black", 250, "Ahmad Tea"))
# print(bakery.add_drink("Tea", "Green", 250, "Lipton"))
#
# print(f"\n\n{'# ADD_TABLE'}")
# print(bakery.add_table("OutsideTable", 52, 10))
# print(bakery.add_table("OutsideTable", 95, 15))
# print(bakery.add_table("InsideTable", 15, 15))
# print(bakery.add_table("InsideTable", 4, 15))
#
# print(f"\n\n{'# RESERVE_TABLE'}")
# print(bakery.reserve_table(12))
#
# print(f"\n\n{'# ORDERS_FOOD'}")
# print(bakery.order_food(95, "Sour", "White", "Chocolate", "Vanilla", "Strawberry", "Hazelnut", "Wholegrain"))
# print(bakery.order_food(34, "Sour", "White", "Chocolate", "Vanilla", "Strawberry", "Hazelnut", "Wholegrain"))
#
# print(f"\n\n{'# ORDERS_DRINK'}")
# print(bakery.order_drink(95, "Spring", "Mineral", "Black", "Green", "White", "Tap", "Fruit"))
#
# print(f"\n\n{'# LEAVE_TABLE'}")
# print(bakery.leave_table(95))
#
# print(f"\n\n{'# GET_TOTAL_INCOME'}")
# print(bakery.get_total_income())
#
# print(f"\n\n{'# TABLES_INFO'}")
# print(bakery.get_free_tables_info())