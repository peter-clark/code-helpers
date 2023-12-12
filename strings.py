def isValid(self, s):
        """
        :checks if a series of brackets ([{}]) are closable and balanced.
        :type s: str
        :rtype: bool
        """
        st = []
        bmap = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in bmap.values():
                st.append(i)
            elif i in bmap.keys():
                if not st or st.pop()!=bmap[i]:
                    return False
        return not st