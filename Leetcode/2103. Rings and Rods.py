class Solution(object):
    def countPoints(self, rings):
        r, g, b = [], [], []
        count = 0
        for i in range(10):
            r.append(rings.count("R"+str(i)))
            g.append(rings.count("G"+str(i)))
            b.append(rings.count("B"+str(i)))

        for i in range(10):
            if r[i] > 0 and g[i] > 0 and b[i] > 0:
                count += 1

        return count
