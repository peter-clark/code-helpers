## Taken from:
# https://leetcode.com/studyplan/leetcode-75/

## Greatest Common Denominator of two strings (shared sequence of char of size gcd) ## 
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        # Validation step
        if str1 + str2 != str2 + str1: 
            return ""
        # Exit case (returning smaller strings in recursion)
        if len(str1) == len(str2):
            return str1
        
        # Select which to recurse by size.
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):]) #return cascade from exit case


## Weave two strings ##
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        new = []
        l = max(len(word1), len(word2))
        
        for i in range(0,l):
            if i<len(word1):
                new.append(word1[i])
            if i<len(word2):
                new.append(word2[i])
            i+=1
        return "".join(new)


## Reverse whole words in list sans spaces
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split(" ")
        s_raw = [word for word in s if word != ""]
        s_new=""
        print(s_raw)
        s=s_raw
        for i in range(len(s)):
            if i!=len(s)-1:
                _s=s[len(s)-1-i]+" "
            else: 
                _s=s[len(s)-1-i]
            s_new += _s
        return s_new

## Find product of elements in a list except own index. ##
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        ans=[1]*n
        pref=[1]*n
        suff=[1]*n
        for i in range(1,n): # Calculate all prefix sums
            pref[i] = pref[i-1] * nums[i-1]
        for i in range(n-2,-1,-1):
            suff[i] = suff[i+1] * nums[i+1]
        for i in range(n):
            ans[i]=pref[i]*suff[i]

        return ans


## if there exists three indicies where i<j<k and nums[i]<nums[j]<nums[k]
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l=len(nums)
        if l<3:
            return False
        first=float('inf')
        second=float('inf')
        for n in nums:
            if n<=first:
                first=n
            elif n<=second:
                second=n
            else:
                return True
        return False    