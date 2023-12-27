# Given an unsorted array of N elements , find any of local minima
# local minima is , if both neighbour elements are greater

# Given an array of integers A, find and return the local minima in it.
# An array element is considered a local minima if it is smaller than its neighbors. 
# For corner elements, we need to consider only one neighbor.

class solution:
    def localMinima(self,arr):
        l = 0
        h = len(arr)-1
        if len(arr)==1:
            return arr[0]
        if len(arr)==2:
            return min(arr[0],arr[1])
        while(l<=h):
            mid =(l+h)//2
            if(arr[mid]< arr[mid+1] and arr[mid]<arr[mid-1]):
                return arr[mid]
            elif arr[mid]>arr[mid-1]:
                h = mid-1
            else:
                l = mid+1
        return -1

# A = [9,8,7,3,6,4,1,5]
# A = [5,4,6,8,2,1,7]
A = [9,8,1,3,6,4,2,5]
obj = solution()
print(obj.localMinima(A))
