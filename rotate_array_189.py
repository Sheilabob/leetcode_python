class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)

        def reverseArray(array, start, end):

            while start < end:
                array[start], array[end] = array[end], array[start]
                start += 1
                end -= 1
            return array

        reverseArray(nums, 0, len(nums)-1)
        reverseArray(nums, 0, k-1)
        reverseArray(nums, k, len(nums)-1)


print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3))


# reversing in place was a challenge, need to reverse the array first before the parts maybe?

# 4/21/22 Runtime: 192 ms, faster than 76.41% of Python online submissions for Rotate Array.
# Memory Usage: 25 MB, less than 36.25% of Python online submissions for Rotate Array.
