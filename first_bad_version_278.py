def isBadVersion(num):
    if num >= 76:
        return True
    else:
        return False


class Solution(object):
    def firstBadVersion(self, n):
        lowest = 1
        highest = n

        while lowest <= highest:
            pivot = (lowest + highest) // 2

            if isBadVersion(lowest) == True:
                return lowest
            if isBadVersion(pivot) == True:
                highest = pivot - 1
            else:
                lowest = pivot + 1

        return lowest


test = Solution().firstBadVersion(502)
print(test)

# 4/19/2022 Runtime: 25 ms, faster than 37.27 % of Python online submissions for First Bad Version.
# Memory Usage: 13.4 MB, less than 61.25 % of Python online submissions for First Bad Version.
