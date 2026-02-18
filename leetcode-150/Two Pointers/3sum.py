class ThreeSum:
    '''
    Solution for the 3 Sum problem.

    I leverage the knowledge from 2 sum problems using 2 pointers.
    The first step is to sort the numbers list.
    I loop through the list of numbers and use each number as an anchor and solve for 2 sum.    
    The main problem arises with the avoiding duplicate results. For that, I start the left pointer always from the location after the anchor location
    I then check whether the current anchor is equal to the previous anchor, if it is, I skip the current anchor and go to the next one. 
    To avoid duplicate numbers inside the solution list like for example [1,2,0,1,0,0,0,0] -> [[0, 0, 0], [0, 0, 0]], I check if the next left pointer is the same as the prev left pointer. If it is, I just increment the left pointer.
    This skipping works because the list is sorted in the beginning
    '''
        
    # def solution(self, nums: list) -> list:
    #     result = []
    #     nums = sorted(nums)
    #     for i, num in enumerate(nums):
    #         l = i+1
    #         r = len(nums)-1
    #         if nums[i] == nums[i-1] and i>0:
    #             continue
    #         while l<r:
    #             sum = num + nums[l] + nums[r]
    #             if sum > 0:
    #                 r-=1
    #             if sum < 0:
    #                 l+=1
    #             if sum == 0:
    #                 result.append([num, nums[l], nums[r]])
    #                 l+=1
    #                 while nums[l] == nums[l-1] and l < r:
    #                     l += 1
    #                 r-=1
        
    #     return result

    def solution(self, nums: list[int]) -> list[list]:
        sorted_nums = sorted(nums)
        result = []
        for i, num in enumerate(nums):
            l = i+1
            r = len(nums)-1
            if nums[i] == nums[i-1] and i>0:
                continue
            while l<r:
                sum = num + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                if sum < 0:
                    l += 1
                if sum == 0:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    r -= 1

        return result
    
if __name__=="__main__":
    nums = [1,2,0,1,0,0,0,0]
    sol = ThreeSum()
    answer = sol.solution(nums)
    print(answer)