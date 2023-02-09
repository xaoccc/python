class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        a = sorted(seats)
        b = sorted(students)
        moves = 0
        for i in range(len(a)):
            moves += abs(a[i] - b[i])
                
        return moves
