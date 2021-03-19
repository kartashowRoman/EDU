def solution(n):
    ### YOUR CODE ###
    deux_list = []
    for i in range(n):
    	mult = 1
    	for j in range(i):
    		mult*=2
    	if mult > n:
    		break
    	deux_list.append(mult)


    return deux_list
