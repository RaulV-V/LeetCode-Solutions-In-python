# I honestly struggled with this problem because I was stuck in the wrong mentallity, the first iteration (2nd here) 
# was very convoluted because i was just fixing the error by inserting more if statements to get all edge cases
# The second iteration was trying to fix that and just intrinsicly skip over duplicate numbers but that still
# didnt address the issue of looping so much. Finally I reevaluated my approach and was able to find the proper
# two pointer approach to achieve O(n) time and O(1) space




class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointA = 0
        pointB = len(numbers) - 1
        while pointA < pointB:
            s = numbers[pointA] + numbers[pointB]
            if s == target:
                return [pointA + 1, pointB + 1]   
            if s < target:
                pointA += 1                  
            else:
                pointB -= 1                  
 
            

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        pointA = 0
        pointB = 1

        while True:
            
            if numbers[pointA] + numbers[pointB] == target:
                return [pointA + 1, pointB + 1]
            if numbers[pointA] + numbers[pointB] > target or pointB >= len(numbers) - 1:
                pointA += 1
                pointB = pointA + 1
                if numbers[pointA] + numbers[pointB] == target:
                    return [pointA + 1, pointB + 1]
                while numbers[pointA] == numbers[pointA + 1] and pointA:
                    pointA += 1
                pointB = pointA + 1
            else:
                pointB += 1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        pointA = 0
        pointB = 1
        valA = -1
        valB = -1
        n = len(numbers)
        while True:

            valA = numbers[pointA]
            valB = numbers[pointB]
            if valA + valB == target:
                return [pointA + 1, pointB + 1]
            else:
                if valA + valB > target or pointB >= n - 1:
                    while valA == numbers[pointA + 1]:
                        pointA += 1
                    pointA += 1
                    pointB = pointA + 1
                else:
                    print(valB, numbers[pointB + 1])
                    while valB == numbers[pointB + 1]:
                        pointB += 1
                        if(pointB >= n - 1):
                            while valA == numbers[pointA + 1]:
                                pointA += 1
                            pointA += 1
                            pointB = pointA
                            break
                    pointB += 1