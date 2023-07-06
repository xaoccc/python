from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def calculate_revenue_after_race(self, race_pos):
        profits = {1: 1500000, 2: 800000, 8: 20000, 10: 10000}
        self.budget += profits[race_pos] - 250000
        return f"The revenue after the race is { profits[race_pos] - 250000 }$. Current budget { self.budget }$"
