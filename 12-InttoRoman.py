# This had a runtime of 0 ms, I tried to keep this solution readable by just going place by place
# since the intructions limited the value to 3499. This could be recreated in to and algorithm 
# but this format contributes to a better readable solution and the case by case checks lend to 
# a fast runtime due to there being no loops greater than 3 iterations and not computationally heavy operations


# This algorithmn runs in O(1) time and O(1) space but some time can be theoretically mitagated by adding 
# additional if statements to jump to which place to start at
class Solution:
    def intToRoman(self, num: int) -> str:
        numeral = {
            1 : "I",
            5 : "V",
            10 : "X",
            50 : "L",
            100 : "C",
            500 : "D",
            1000 : "M",
        }

        # Thousands:
        roman = ""
        roman += "M" * (num // 1000)
        valuplace = 0

        # Hundreds:
        valueplace = (num // 100) % 10
        if valueplace == 4:
            roman += "CD"
        elif valueplace == 9:
            roman += "CM"
        else:
            if valueplace // 5 > 0:
                valueplace -= 5
                roman += "D"
            while valueplace > 0:
                valueplace -= 1
                roman += "C"
        # Tens:
        valueplace = (num // 10) % 10
        if valueplace == 4:
            roman += "XL"
        elif valueplace == 9:
            roman += "XC"
        else:
            if valueplace // 5 > 0:
                valueplace -= 5
                roman += "L"
            while valueplace > 0:
                valueplace -= 1
                roman += "X"     
        
        # Ones
        valueplace = num % 10
        if valueplace == 4:
            roman += "IV"
        elif valueplace == 9:
            roman += "IX"
        else:
            if valueplace // 5 > 0:
                valueplace -= 5
                roman += "V"
            while valueplace > 0:
                valueplace -= 1
                roman += "I"     
        return roman