class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return list(filter(lambda x: x < pivot, nums)) + list(filter(lambda x: x == pivot, nums)) + list(filter(lambda x: x > pivot, nums))
