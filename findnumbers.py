#https://leetcode.com/problems/find-numbers-with-even-number-of-digits/submissions/
def findNumbers(self, nums: List[int]) -> int:
    count = 0
    for _, num in enumerate(nums): #O(N)
        if len(str(num)) % 2 == 0: #len O(1) operation in python str o(s)
            count += 1 # O(1)
            
    return count #O(1)
   
   #Overall runtime complexity O(N + S)

# Space complexity O(1)