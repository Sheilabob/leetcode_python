class Solution(object):
    def rotate(self, nums, k):
        subarray1 = nums[0: len(nums)-k: 1]
        subarray2 = nums[len(nums)-k::1]

        def reverseArray(array):
            start = 0
            end = len(array)-1
            while start < end:
                array[start], array[end] = array[end], array[start]
                start += 1
                end -= 1
            return array

        newsub1 = reverseArray(subarray1)
        newsub2 = reverseArray(subarray2)
        backwardssolution = newsub1 + newsub2
        solution = reverseArray(backwardssolution)

        return solution


test = Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)
print(test)
