class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not (len(s) == len(t)):
            return False
        else:
            ss = sorted(s)
            tt = sorted(t)
            for i in range(len(s)):
                if ss[i]!=tt[i]:
                    return False
            return True
        