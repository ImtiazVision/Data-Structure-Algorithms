class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Using the first element, we will initialize our variables.
        current_subarray = max_subarray = nums[0]
        
        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            #If current subarray is negative, it should be discarded. Otherwise, continue to add to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray
