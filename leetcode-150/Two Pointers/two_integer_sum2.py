class TwoSum2:
    """
        Solution for the sorted two sum problem. 
        
        I'm utilizing the fact that the numbers are sorted in ascending order. 
        I first compute the sum and if that is equal to the target, i return the two elements
        If the sum is less than the target, I increment the left pointer by 1
        If the sum is higher than the target, I decrement the right pointer by 1
        """       

    def solution(self, nums: list[int], target: int) -> list[int]:
        l = 0
        r = len(nums) - 1
        while l < r:
            sum = nums[l] + nums[r]
            if sum > target:
                r -= 1
            if sum < target:
                l += 1
            if sum == target:
                return [l+1, r+1]
    
if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    sol = TwoSum2()
    answer = sol.solution(nums, target)
    print(answer)