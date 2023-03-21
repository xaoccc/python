class Solution(object):
    def countGoodRectangles(self, rectangles):
        sqares = []
        for i in rectangles:
            sqares.append((min(i)))
        return sqares.count(max(sqares))