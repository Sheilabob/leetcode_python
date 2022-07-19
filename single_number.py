class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    del nums[i]
                    del nums[j]
        return nums[0]

test = Solution().singleNumber([2,2,1])
print(test)