class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

        # I AM SO STUCK!!

# Watched a video:

# submitted 5/4

# Runtime: 51 ms, faster than 63.15% of Python online submissions for Valid Anagram.
# Memory Usage: 15.3 MB, less than 18.65% of Python online submissions for Valid Anagram.

# shortcut:  return sorted(s) == sorted(t), uses less memory, but is slower
