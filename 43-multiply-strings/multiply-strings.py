class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_1 = 0
        num_2 = 0
        place_value = 0
        n1 = len(num1)
        n2 = len(num2)
        i = n1 - 1
        j = n2 - 1
        while i >= 0:
            num_1 += int(num1[i])*(10**place_value)
            place_value += 1
            i -= 1
        place_value = 0
        while j >= 0:
            num_2 += int(num2[j])*(10**place_value)
            place_value += 1
            j -= 1
        return str(num_1*num_2)