class Solution:
    def getMinMax(self, arr):
        # code here
        min=arr[0]
        max=0
        for i in range(len(arr)):
            if arr[i]>max:
                max=arr[i]
            elif arr[i]<min:
                min=arr[i]
        return [min,max]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna