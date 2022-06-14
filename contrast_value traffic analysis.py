def contrast(speeds):
    N = len(speeds)-1
    M = max(speeds)
    matrix = np.zeros([M,M],dtype = float)
    print()
    for x in range(0,N):
        z = speeds[x]-1
        v = speeds[x+1]-1
        temp = 1/N
        np.set_printoptions(precision=2)
        matrix[z][v] += temp
    print(matrix)
    
    contrast_value = 0
    for i in range (0,M):
        for j in range (0,M):
            if(matrix[i][j]>0):
                temp = (j-i)*abs(i-j)*matrix[i][j]
                contrast_value += temp
    return(contrast_value)

        

print(contrast([10,10,7,10,8,9,10,10,8,8]))