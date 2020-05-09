    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l = 0
        r = len(A) - 1
        while l < r:
            
            # traverse till we find an odd value
            while A[l] % 2 == 0 and l < r:
                l +=1 
                
            # traverse till we find an even value
            while A[r] % 2 != 0 and l < r:
                r -= 1
            #swap
            if l < r:
                tmp = A[l]
                A[l] = A[r]
                A[r] = tmp
                
        return A
    #TIme complexity O(N)
    #Space complexity O(o + e) where o is odd list and e is even list