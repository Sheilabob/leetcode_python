class Solution(object):
    def moveZeroes(self, nums):
        lowest = 0
        highest = len(nums)

        while lowest < highest:

            if nums[lowest] == 0:
                nums.append(nums[lowest])
                nums.remove(nums[lowest])
                highest -= 1
            else:
                lowest += 1

        return nums

#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """


test = Solution().moveZeroes([0, 1, 0, 3, 12])
print(test)

# Submitted 4/20/22
# Runtime: 695 ms, faster than 19.37% of Python online submissions for Move Zeroes.
# Memory Usage: 14.9 MB, less than 13.91% of Python online submissions for Move Zeroes.

# This was super slow and used a lot of memory, but it did use two-pointers and it didn't move the array . . .

# Youtube solution:

# class Solution(object):
#     def moveZeroes(self, nums):
#         left = 0

#         for right in range(len(nums)):
#             if nums[right] != 0:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 left += 1

#         return nums


# test = Solution().moveZeroes([0, 1, 0, 3, 12])
# print(test)

# Used less memory by far, not much faster:
# Runtime: 231 ms, faster than 34.03% of Python online submissions for Move Zeroes.
# Memory Usage: 14.6 MB, less than 60.89% of Python online submissions for Move Zeroes.
