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
            lasers += beams_start * sum(row) if beams_start != 0 else 0
            beams_start = sum(row)

        return lasers