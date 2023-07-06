from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def calculate_revenue_after_race(self, race_pos):
        profits = {1: 1000000, 3: 500000, 5: 100000, 7: 50000}
        self.budget += profits[race_pos] - 200000
        return f"The revenue after the race is { profits[race_pos] - 200000 }$. Current budget { self.budget }$"
