class Solution(object):
    def searchInsert(self, nums, target):
        lowest = 0
        highest = len(nums)-1

        if nums[0] > target:
            return 0

        while lowest <= highest:
            pivot = (lowest + highest) // 2
            pivot_value = nums[pivot]

            if pivot_value == target:
                return pivot
            if pivot_value > target and nums[pivot-1] < target:
                return pivot
            if pivot_value > target:
                highest = pivot-1
            else:
                lowest = pivot + 1

        return len(nums)


test = Solution().searchInsert([1, 3, 5, 6], 5)
test2 = Solution().searchInsert([1, 3, 5, 6], 2)
test3 = Solution().searchInsert([1, 3, 5, 6], 7)

print(test, test2, test3)

# 4/19/2022 Runtime: 48 ms, faster than 42.01% of Python online submissions for Search Insert Position.
# Memory Usage: 14.2 MB, less than 26.03% of Python online submissions for Search Insert Position.

# First submission failed to take into account if the target was lower that the first number in the list, added lines 6-7
