class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        good_triplets = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)): 
                if abs(arr[i] - arr[j]) <= a:              
                    for k in range(j+1, len(arr)):
                        if abs(arr[i] - arr[k]) <= c and abs(arr[j] - arr[k]) <= b:
                            good_triplets += 1
        return good_triplets
