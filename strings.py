def isClosedBrackets(self, s):
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


def repeatedSubstringPattern(self, s):
    """
    :type s: str
    :rtype: bool
    """
    # Concat s with itself. (s+s)
    # Check if s exists, removing first and last char of concat
    # If s exists in concat[1:-1], it is a substring repeated
    return s in (s + s )[1: -1]

def addBinary(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    return bin(int(a,2)+int(b,2))[2::]
        