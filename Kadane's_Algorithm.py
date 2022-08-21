def maxSubArraySum(self,arr,N):
        ##Your code here
        
        max_c=max_g=arr[0]
        for i in range (1,N):
            max_c=max(arr[i], max_c+arr[i])
            if max_c > max_g:
                max_g=max_c
         
        if max_g>=0:
            return max_g;
        else:
            return 0;
