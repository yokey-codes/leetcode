class Solution:
    def countDigits(self, num: int) -> int:
        temp=num
        tot=0
        while temp>0:
            digit=temp%10
            if num%digit==0:
                tot+=1
            temp//= 10
        return tot

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna