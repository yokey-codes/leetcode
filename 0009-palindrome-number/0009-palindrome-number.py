class Solution:
    def isPalindrome(self, x: int) -> bool:
            org=x
            rev=0
            if x<0:
                return False
            if x==0:
                return True
            while x>0:
                n=x%10
                rev=rev*10+n
                x=x//10
            return org == rev
                


            