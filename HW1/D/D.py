def solution(total):
    ### YOUR CODE HERE ###
    hours = total % 1440 // 60
    minutes = total % 1440 % 60
    return str(hours)+" "+str(minutes)
