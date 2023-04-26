# Wave Array
A = [19]
# ans = 2 1 4 3 5 
n = len(A)
B = [0]*n
A.sort()
# print(A)
if(n==1):
    print(A)
for i in range(0,n-1,2):
    if A[i]<=A[i+1]:
        B[i] = A[i+1]
        B[i+1] = A[i]
    if(i==n-3):
        B[i+2] = A[i+2]
print(B)