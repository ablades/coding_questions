# Restate the problem
# Ask clarifying questions
# State assumptions
# Explain rational/discuss tradeoffs
# Suggest imporovements

class Solution:
    #https://leetcode.com/problems/two-sum/
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Return the indexes of two numbers that sum up to the value we're looking for.
        #Can the list be empty? are there duplicates? Can we use the same element twice? Are there multiple solutions?
        #Can numbers be neagative? Is the list sorted? Can the target not be in the list?
        #I assume that duplicates may exisit in the list but cannot be used. The list is not sorted. There are not mu;tiple solutions, etc
        
        #loop over all items
            #calculate target - value.
                #look for that value in the hash table
                #if found return the value aka index
                #if not found add current item to hash table.
        # this algorithm has a run time complexity of O(N) since it must iterate over an entire list.
        # the space complexity also isn't as great as its O(N) due to allocating a hashmap equal to size n as we iterate.
        # if we find the target early we can exit and that will save some space

    
if __name__ == "__main__":