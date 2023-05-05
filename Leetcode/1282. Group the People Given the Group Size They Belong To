class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        work_list = groupSizes.copy()
        result = []
        used_idxs = []

        i = 0
        while groupSizes:
            current = min(groupSizes)
            result.append([])
            for j in range(len(work_list)):
                if work_list[j] == current and j not in used_idxs:
                    result[i].append(j)
                    used_idxs.append(j)
                    del groupSizes[groupSizes.index(current)]
                if len(result[i]) == current:
                    break
                    
            i += 1
        return result
