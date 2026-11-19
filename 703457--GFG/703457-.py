class Solution:
    def getMinMax(self, arr):
        
        mn = float('inf')
        mx = float('-inf')
        
        for num in arr:
            # Updating the minimum value
            mn = min(num, mn)

            # Updating the maximum value
            mx = max(num, mx)

        # Returning the minimum and maximum values
        return [mn, mx]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna