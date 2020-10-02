def slidingwindow(arr,k):
    
    ng = nextGreater(arr)
    
    
    j=0
    
    for i in range(len(arr)-k+1):
 
        
        j = i
        
        while (ng[j] < i + k):
            j = ng[j]
        
        print(arr[j])
            

def nextGreater(arr):
    
    stack = []
    stack.append(len(arr)-1)
    ans = [None]*len(arr)
    arr[-1] = len(arr)
    
    for i in range(len(arr)-2,-1,-1):
        
        while len(stack)>0 and arr[stack[-1]] < arr[i]:
            stack.pop()
            
        if len(stack)==0:
            ans[i] = len(arr)
        else:
            ans[i] = stack[-1]
            
        stack.append(i)
    return ans
    



n = int(input())
arr=[]
for i in range(n):
    x = int(input())
    arr.append(x)
    
k = int(input())


slidingwindow(arr,k)
