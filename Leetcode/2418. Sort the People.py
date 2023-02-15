class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        final_list = []
        sorted_list = []

        for i in range(len(names)):
            new_list = []
            new_list.append(heights[i])
            new_list.append(names[i])
            final_list.append(new_list) 
        final_list = list(sorted(final_list))
        final_list.reverse()
        for i in range(len(final_list)):
            sorted_list.append(final_list[i][1])
        return sorted_list
