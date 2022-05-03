class Solution(object):
    def isAnagram(self, s, t):
        holder1 = []
        holder2 = []
        for l in range(0, len(s)):
            holder1.append(s[l])
        for l in range(0, len(t)):
            holder2.append(t[l])
        for x in range(0, len(holder2)):
            for y in range(0, len(holder1)):
                if holder2[x] == holder1[y]:
                    holder1.remove(holder1[y]),
                    holder2.remove(holder2[x])
        if len(holder1) == 0 and len(holder2) == 0:
            return True
        else:
            return False

            # I AM SO STUCK!!
