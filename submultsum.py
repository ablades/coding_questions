#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/submissions/
def subtractProductAndSum(self, n: int) -> int:
        
        digits = [int(x) for x in str(n)]
        mult = 1
        sum = 0
        for digit in digits:
            mult *= digit
            sum += digit
            
        return mult - sum

"""
Variable Table 
n = 234
--------------------
digits = [2, 3, 4]
mult : 1
sum : 0
--------------------
mult : 2
sum : 2
------------------
mult : 6
sum : 5
------------------
mult : 24
sum : 9
------------------
return -> result : 15

"""