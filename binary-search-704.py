class Solution(object):
    def search(self, nums, target):
        lowest = 0
        highest = len(nums)-1

        while lowest <= highest:
            pivot = (lowest + highest) // 2
            pivot_value = nums[pivot]

            if pivot_value == target:
                return pivot
            if pivot_value > target:
                highest = pivot-1
            else:
                lowest = pivot + 1

        return -1


tryout1 = Solution().search([-1, 0, 3, 5, 9, 12], 9)
tryout2 = Solution().search([-1, 0, 3, 5, 9, 12], 2)

print(tryout1, tryout2)

# 4/19/2022 Runtime: 217 ms, faster than 65.58% of Python online submissions for Binary Search.
# Memory Usage: 14.5 MB, less than 79.32% of Python online submissions for Binary Search.
