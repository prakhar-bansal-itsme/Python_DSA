class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        point = len(s) - 1

        add = ""
        ans = ""

        for i in range(len(s) -1, -1, -1):
           
            if s[i] != " ":
                add += s[i]

            if s[i] and s[i-1] == " ":
                continue

            if s[i] == " ":
                add = add[::-1]
                ans += add + " "
                add = ""
            if i == 0:
                add = add[::-1]
                ans += add
        return ans
            
