class ContainerWithMostWater:
    '''
    Solution for Container with most water problem

    The concept is that the area depends on the shorter line. So, we have to move the shorter line in order to try and achieve a larger area as moving the larger line while keeping the shorter line intact wont change the area.

    Here, I use two pointers to check which pointer has the lower height
    if the left pointer has a lower height, i increment it
    if the right pointer has a lower height, I decrement it
    This way, the whole 
    '''
    def solution(self, heights: list[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = -1
        while l<r:
            new_area = min(heights[l], heights[r]) * (r-l)
            max_area = max(new_area, max_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
    
if __name__ == "__main__":
    heights = [1,8,6,2,5,4,8,3,7]
    sol = ContainerWithMostWater()
    answer = sol.solution(heights)
    print(answer)

