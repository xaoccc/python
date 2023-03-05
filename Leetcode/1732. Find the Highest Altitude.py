class Solution(object):
    def largestAltitude(self, gain):
        max_alt = -999999
        current_altitude = 0
        for i in range(len(gain)):
            current_altitude += gain[i]
            if current_altitude > max_alt:
                max_alt = current_altitude
        if max_alt > 0:
            return max_alt
        else:
            return 0