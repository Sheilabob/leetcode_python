class Solution(object):
    def twoSum(self, nums, target):
        indeces = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    indeces.append(i)
                    indeces.append(j)
        return indeces

# Submitted 5/3/22
# Runtime: 3751 ms, faster than 21.17% of Python online submissions for Two Sum.
# Memory Usage: 14.5 MB, less than 10.25% of Python online submissions for Two Sum.

# Youtube solution:

# class Solution(object):
#     def twoSum(self, nums, target):
#         prev_map = {}

#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in prev_map:
#                 return[prev_map[diff], i]
#             prev_map[n] = i
#         return

# MUCH FASTER
