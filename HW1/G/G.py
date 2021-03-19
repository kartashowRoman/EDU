def solution(a, b):
    ### YOUR CODE ###
    list_sum = a + b
    to_delete = [i for i in b if i in a]
    for i in to_delete:
    	list_sum.remove(i)
    list_sum.sort()
    return list_sum
