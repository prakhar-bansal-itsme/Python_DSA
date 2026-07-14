class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 == 1:
            return False
        
        st = []
        for ch in list(s):
            # for opening blacket
            if ch == '(' or ch == '[' or ch == '{':
                st.append(ch)
            #for closing bracket
            else:
                if len(st) == 0:
                    return False
                top = st.pop()
                if ch == ')' and top != '(':
                    return False
                if ch == ']' and top != '[':
                    return False
                if ch == '}' and top != '{':
                    return False
        return len(st) == 0