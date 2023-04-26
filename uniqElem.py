A = [ 1, 1, 2, 2, 3 ]
n = len(A)
l = 0
h = n-1
# print('n=',n)
while(l<=h):
    mid = (l+h)//2
    # print('mid===',mid)
    if mid==0 or mid==n-1:
        break
    if (A[mid]==A[mid-1]):
        f_occ = mid-1
        if(f_occ&1):
            h = mid-1
        else:
            l = mid+1
    elif (A[mid]==A[mid+1]):
        f_occ = mid
        if(f_occ&1):
            h = mid-1
        else:
            l= mid+1
    else:
        # print('unique=',mid)
        break
print('unique index=',mid)