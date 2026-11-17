class Solution:
    def countDigits(self, num: int) -> int:
        c=0
        for i in str(num):
            if num%int(i)==0:
                c+=1
        return c        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna