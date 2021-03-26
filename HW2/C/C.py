def solution(arr):
    ### YOUR CODE ###
    
    res = []
    if len(arr) == 0:
    	return res
    row_begin = 0
    row_end = len(arr)-1
    col_begin = 0
    col_end = len(arr[0])-1

    while row_begin <= row_end and col_begin <= col_end:
        for i in range(col_begin, col_end+1):
            res.append(arr[row_begin][i])
        row_begin += 1

        for i in range(row_begin, row_end+1):
            res.append(arr[i][col_end])
        col_end -= 1

        if row_begin <= row_end:
            for i in range(col_end, col_begin-1, -1):
                res.append(arr[row_end][i])
        row_end -= 1

        if col_begin <= col_end:
            for i in range(row_end, row_begin-1, -1):
                res.append(arr[i][col_begin])
        col_begin += 1
 
    return res



    