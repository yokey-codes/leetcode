class Solution:
    def getMinMax(self, arr):
        
        sort=[]
        
        while len(arr)>0:
            min=arr[0]
            
            for i in range(len(arr)):
                if arr[i]<min:
                    min=arr[i]
                
            sort.append(min)
            arr.remove(min)
        
        return [sort[0],sort[-1]]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna