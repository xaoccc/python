class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        kf = []
        kf.extend((celsius + 273.15, celsius * 1.80 + 32))
        return kf
