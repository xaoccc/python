class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        beams_start = 0
        lasers = 0

        for row in bank:
            if "1" not in row:
                continue
            row = [int(i) for i in row]

            if sum(row) != 0 and beams_start == 0:
                beams_start = sum(row)

            elif sum(row) != 0 and beams_start != 0:
                lasers += beams_start * sum(row)
                beams_start = sum(row)

        return lasers