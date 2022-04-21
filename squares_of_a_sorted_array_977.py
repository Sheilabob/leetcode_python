class Solution(object):
    def sortedSquares(self, nums):
        start = 0
        end = len(nums)-1
        result = [0]*len(nums)
        index = len(nums)-1

        while end >= 0 and index >= 0:
            if abs(nums[start]) > abs(nums[end]):
                result[index] = nums[start] * nums[start]
                start += 1
            else:
                result[index] = nums[end] * nums[end]
                end -= 1
            index -= 1
        return result


test = Solution().sortedSquares([-4, -1, 0, 3, 10])

# Figuring out how to start with an empty array of the correct length to put the solution into was a challenge

# 4/20/22 Runtime: 230 ms, faster than 53.79% of Python online submissions for Squares of a Sorted Array.
# Memory Usage: 15.6 MB, less than 33.57% of Python online submissions for Squares of a Sorted Array.
