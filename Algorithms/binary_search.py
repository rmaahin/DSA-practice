def binary_search(nums, to_find):
    left_index = 0
    right_index = len(nums)-1
    mid_index = 0
    
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2 
        mid_number = nums[mid_index]

        if mid_number == to_find:
            return mid_index
        elif mid_number < to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
        
    return -1

def binary_search_recursive(nums, to_find, left_index, right_index):
    if right_index < left_index:
        return -1
    
    mid_index = (left_index + right_index) // 2
    
    if mid_index >= len(nums):
        return -1
    
    mid_number = nums[mid_index]

    if mid_number == to_find:
        return mid_index
    
    if mid_number < to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1
    
    return binary_search_recursive(nums, to_find, left_index, right_index)

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    to_find = 12
    index = binary_search(nums, to_find)
    index_recursive = binary_search_recursive(nums, to_find, 0, len(nums))
    print(index)
    print(index_recursive)