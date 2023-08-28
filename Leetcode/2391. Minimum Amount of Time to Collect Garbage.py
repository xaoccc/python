class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        glass_truck, paper_truck, metal_truck = 0, 0, 0
        glass_end, paper_end, metal_end = -1, -1, -1
        glass, paper, metal = False, False, False

        for i in range(len(garbage)):

            if "G" in garbage[i]:
                glass_truck += garbage[i].count("G")

            if "P" in garbage[i]:
                paper_truck += garbage[i].count("P")

            if "M" in garbage[i]:
                metal_truck += garbage[i].count("M")

        for i in range(len(garbage) - 1, -1, -1):
            if "G" in garbage[i]:
                if not glass:
                    glass_end = i
                    glass = True

            if "P" in garbage[i]:
                if not paper:
                    paper_end = i
                    paper = True

            if "M" in garbage[i]:
                if not metal:
                    metal_end = i
                    metal = True

        if glass_end > -1:
            glass_truck += sum(travel[:glass_end])
        if paper_end > -1:
            paper_truck += sum(travel[:paper_end])
        if metal_end > -1:
            metal_truck += sum(travel[:metal_end])
        return glass_truck + paper_truck + metal_truck