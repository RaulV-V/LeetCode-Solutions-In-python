class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        downBound = len(matrix)
        rightBound = len(matrix[0]) 
        upBound = 0
        leftBound = 0
        output = [0] * (downBound * rightBound)
        num = 0
        while downBound > upBound and rightBound > leftBound:

            for i in range(leftBound, rightBound):
                output[num] =  matrix[upBound][i]
                num += 1
            upBound += 1

            for i in range(upBound, downBound):
                output[num] = matrix[i][rightBound - 1]
                num += 1
            rightBound -= 1

            if upBound < downBound:
                for i in reversed(range(leftBound, rightBound)):
                    output[num] = matrix[downBound - 1][i]
                    num += 1
                downBound -= 1
            
            if leftBound < rightBound:
                for i in reversed(range(upBound, downBound)):
                    output[num] = matrix[i][leftBound]
                    num += 1
                leftBound += 1

        return output