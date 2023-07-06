from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def calculate_revenue_after_race(self, race_pos):
        revenue, expences = 0, 250000
        sponsors_profits = {"Oracle": {1: 1500000, 2: 800000}, "Honda": {8: 20000, 10: 10000}}
        for sponspor, profit in sponsors_profits.items():
            for position, money in profit.items():
                if race_pos <= position:
                    revenue += money
                    break
        revenue -= expences
        self.budget += revenue
        return f"The revenue after the race is { revenue }$. Current budget { self.budget }$"
