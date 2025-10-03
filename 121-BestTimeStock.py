class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        biggest = 0
        pointA = 0
        pointB = 1
        while pointB < len(prices):
            if prices[pointA] > prices[pointB]:
                pointA = pointB
            else:
                if prices[pointB] - prices[pointA] > biggest:
                    biggest = prices[pointB] - prices[pointA]
            pointB += 1
        return biggest