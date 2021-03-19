def solution(arr):
    ### YOUR CODE ###
    count = 1
    res = []
    for i in range(len(arr)):
    	if arr[i] == arr[i-1]:
    		count+=1
    	else:
    		res.append(count)
    		count = 1
    return max(res, default = 1)