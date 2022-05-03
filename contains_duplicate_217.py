class Solution(object):
    def containsDuplicate(self, nums):
        answer = False
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    answer = True
        return answer

# submitted 5/2/22 Time limit exceeded

# Also tried:
# class Solution(object):
#     def containsDuplicate(self, nums):
#         for i in range (0, len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#         return False;

# This is the solution that worked in time:

# class Solution(object):
#     def containsDuplicate(self, nums):
#         hashset = set()

#         for n in nums:
#             if n in hashset:
#                 return True
#             hashset.add(n)
#         return False

# Runtime: 393 ms, faster than 79.70% of Python online submissions for Contains Duplicate.
# Memory Usage: 24 MB, less than 43.06% of Python online submissions for Contains Duplicate.
