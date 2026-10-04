class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cd_s = {}
        cd_t = {}
        sc=0

        if len(s) != len(t):
            print(False)
        else:
            for i in s:
                if i not in cd_s:
                    fq = 1
                    cd_s[i]=fq
                else:
                    fq = cd_s[i]
                    fq = fq + 1
                    cd_s[i] = fq
            for i in t:
                if i not in cd_t:
                    fq = 1
                    cd_t[i]=fq
                else:
                    fq = cd_t[i]
                    fq = fq + 1
                    cd_t[i] = fq
            for i in cd_s:
                if i not in cd_t:
                    return(False)
                elif (cd_s[i] != cd_t[i]):
                    return(False)
                else:
                    sc=sc+cd_s[i]

        if (sc==len(s)):
            return(True)
        else:
            return(False)
        