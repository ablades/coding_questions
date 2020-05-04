#https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
def numberOfSteps (self, num: int) -> int:
        count = 0
        while num != 0:
            #Is even number
            if num % 2 == 0:
                num = num / 2
            else:
                num -= 1
                
            count += 1
            
        return count

"""
Variable Table 
--------------------
num : 17
count : 0
--------------------
num : 16
count : 1
------------------
num : 8
count : 2
------------------
num : 4
count : 3
------------------
num : 2
count : 4
------------------
num : 1
count : 5
------------------
num : 0
count : 6
------------------
return -> 6
"""