
class Solution(object):
    def topKFrequent(self, nums, k):
        count_nums = {}

        for i in range(len(nums)):
            count_nums[nums[i]] = 1 + count_nums.get(nums[i], 0)
        sorted_count = sorted(count_nums.items(),
                              key=lambda x: x[1], reverse=True)

        most_frequent = []

        for x in range(0, k):
            most_frequent.append(sorted_count[x][0])

        return most_frequent


tryout1 = Solution().topKFrequent([1, 1, 1, 2, 2, 3, 3, 3, 3, 3], 2)

print(tryout1)


# submitted 5/5/22

# Runtime: 107 ms, faster than 55.96% of Python online submissions for Top K Frequent Elements.
# Memory Usage: 16.7 MB, less than 86.44% of Python online submissions for Top K Frequent Elements.

# Youtube solution:
# class Solution(object):
#     def topKFrequent(self, nums, k):
#         count = {}
#         freq = [[] for i in range(len(nums) + 1)]

#         for n in nums:
#             count[n] = 1 + count.get(n, 0)
#         for n, c in count.items():
#             freq[c].append(n)

#         res = []
#         for i in range(len(freq) - 1, 0, -1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res
