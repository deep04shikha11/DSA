# return boundary of rectangular matrix in clockwise direction
def main():    
    n = int(input())
    m = n
    A = []
    for i in range(n):
        inrAry = []
        s = input()
        s = s.split()
        for j in range(n):
            inrAry.append(int(s[j]))
        A.append(inrAry)
    B = 0
    x = 0
    y = 0
    dirc = 'right'
    i = 0
    while(i<(n*m)):
        i += 1
        if(x<n and y<m and x>=0 and y>=0):
            print(A[x][y], end=' ')
        if dirc == 'right':
            if y == m-1-B:
                dirc = 'down'
                x += 1
            else:
                y += 1
        elif dirc == 'down':
            if x== n-1-B:
                dirc = 'left'
                y -= 1
            else:
                x += 1
        elif dirc == 'left':
            if y == B:
                dirc = 'up'
                x -= 1
            else:
                y -= 1
        elif dirc == 'up':
            if x == B+1:
                dirc = 'right'
                y += 1
                B += 1
            else:
                x -= 1

    return 0

if __name__ == '__main__':
    main()