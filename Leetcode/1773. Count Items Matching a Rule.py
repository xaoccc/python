class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        sum = 0

        for item in range(len(items)):
            if ruleKey == "type":
                if items[item][0] == ruleValue:
                    sum += 1

            elif ruleKey == "color":
                if items[item][1] == ruleValue:
                    sum += 1

            elif ruleKey == "name":
                if items[item][2] == ruleValue:
                    sum += 1
        return sum
