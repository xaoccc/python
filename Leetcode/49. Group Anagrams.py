class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}

        for item in strs:
            sorted_item = ''.join(sorted(item))
            if sorted_item not in my_dict:
                my_dict[sorted_item] = []
            my_dict[sorted_item].append(item)

        return list(my_dict.values())