class Solution(object):
    def isAnagram(self, s, t):
        holder = []
        for l in range(0, len(s)):
            holder.append(s[l])
        if len(s) == len(t):
            for x in range(0, len(t)):
                for y in range(0, len(s)):
                    if t[x] == s[y]:
                        if t[x] in holder:
                            holder.remove(t[x])
                        else:
                            return False
        if len(holder) == 0:
            return True
        else:
            return False

            # I AM SO STUCK!!
