class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Checks if an input array is a palindrome or not.
        Implemented using two pointers. 

        - The first "brute" force solution which is commented out works but it occupies additional space and the runtime is large on leetcode.

        - The second one is a more elegant solution that does not occupy additional space so space complexity is O(1) and time complexity is O(n).
        '''

        # filtered_s = [char.lower() for char in s if char.isalnum()]
        # print(filtered_s)
        # i = 0
        # j = len(filtered_s)-1
        # count = 0
        
        # while i<j:
        #     # print(i, j)
        #     if filtered_s[i] == filtered_s[j]:
        #         i += 1
        #         j -= 1
        #         count += 1

        
        # if count == (len(filtered_s) // 2):
        #     return True
        
        # return False

        l = 0
        r = len(s) - 1
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1

            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                return False
        
        return True
    
    def solution(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l<r:
            if s[l] == s[r]:
                l+=1 
                r-=1
            else:
                return False
            while l<r and not s[l].isalnum():
                l+=1 
            while l<r and not s[r].isalnum():
                r-=1


if __name__=="__main__":
    s = "A man, a plan, a canal: Panamaa"
    sol = Solution()
    answer = sol.isPalindrome(s)
    print(answer)