from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def calculate_revenue_after_race(self, race_pos):
        revenue, expences = 0, 200000
        sponsors_profits = {"Petronas": {1: 1000000, 3: 500000}, "TeamViewer": {5: 100000, 7: 50000}}
        for sponspor, profit in sponsors_profits.items():
            for position, money in profit.items():
                if race_pos <= position:
                    revenue += money 
                    break
        revenue -= expences
        self.budget += revenue
        return f"The revenue after the race is { revenue }$. Current budget { self.budget }$"
