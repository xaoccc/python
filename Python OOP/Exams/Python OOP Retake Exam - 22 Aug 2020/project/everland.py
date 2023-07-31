from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum([(room.expenses + room.room_cost) for room in self.rooms])
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            total_expenses = (room.expenses + room.room_cost)
            if room.budget >= total_expenses:
                room.budget -= total_expenses
                result.append(f"{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

        return "\n".join(result)

    def status(self):
        all_people = sum([room.members_count for room in self.rooms])
        result = [f"Total population: {all_people}"]
        for room in self.rooms:
            result.append(f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            children_cost = 0
            if room.children:
                n = 1
                for child in room.children:
                    children_cost += child.get_monthly_expense()
                    result.append(f"--- Child {n} monthly cost: {child.get_monthly_expense():.2f}$")
                    n += 1
            result.append(f"--- Appliances monthly cost: {room.expenses - children_cost:.2f}$")

        return "\n".join(result)



