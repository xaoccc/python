class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        glass_truck, paper_truck, metal_truck = 0, 0, 0
        glass_end, paper_end, metal_end = -1, -1, -1
        glass, paper, metal = False, False, False
        garbage_len = len(garbage)


        for i in range(garbage_len):

            if "G" in garbage[i]:
                glass_truck += garbage[i].count("G")

            if "G" in garbage[garbage_len - i - 1]:
                if not glass:
                    glass_end = garbage_len - i - 1
                    glass = True

            if "P" in garbage[i]:
                paper_truck += garbage[i].count("P")

            if "P" in garbage[garbage_len - i - 1]:
                if not paper:
                    paper_end = garbage_len - i - 1
                    paper = True

            if "M" in garbage[i]:
                metal_truck += garbage[i].count("M")

            if "M" in garbage[garbage_len - i - 1]:
                if not metal:
                    metal_end = garbage_len - i - 1
                    metal = True


        glass_truck += sum(travel[ :glass_end ]) if glass_end > -1 else 0
        paper_truck += sum(travel[ :paper_end ]) if paper_end > -1 else 0
        metal_truck += sum(travel[ :metal_end ]) if metal_end > -1 else 0
        return glass_truck + paper_truck + metal_truck