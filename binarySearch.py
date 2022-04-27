"""
Binary search is a basic method that compares the target value to the array's middle member.

If the goal value equals the center element, we're done.



If the goal value is lower, continue to search on the left.



If the goal value is higher, continue searching on the right.

"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1
