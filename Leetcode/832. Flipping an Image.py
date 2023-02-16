class Solution:
    def flipAndInvertImage(self, image: List[List[int]]):
        for i in range(len(image)):
            image[i].reverse()
            for j in range(len(image[i])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image
