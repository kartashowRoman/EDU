def solution(x):
    ### YOUR CODE ###
    #first step
    x_del = list(x[0:]) 
    del x_del[::3]
    x_del = ''.join(x_del)
    x_whole = x[0]+x_del

    #second
    
    first_index = x_whole.find('h')
    last_index = x_whole.rfind('h')
    x_whole_upper = x_whole[first_index:last_index].replace('h', 'H')
    x_whole = x_whole[:first_index] + x_whole_upper + x_whole[last_index:]

    #third
    x_whole = x_whole.replace('1', 'one')

    return x_whole
