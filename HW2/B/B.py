def solution(x):
    ### YOUR CODE ###
    #first step
    x_del = list(x[0:]) 
    del x_del[::3]
    x_del = ''.join(x_del)
    x_whole = x[0]+ x_del

    #second
    
    
    last_index = x_whole.rfind('h')
    x_whole_upper = x_whole[:last_index].replace('h', 'H')
    x_whole = x_whole_upper + x_whole[last_index:]
    x_whole = x_whole.replace('H', 'h', 1)


    #third
    x_whole = x_whole.replace('1', 'one')

    

    return x_whole

'''
Expected:
bl9kittcrzk0qqqwrdrdwdrfdwtqroc05qbzkli0vkHb3frfqb3fl3wzr90ifbvtz005Htovv03wzwq9lfctcwfonekciwid5o3vtqz3dwHlv3illwv0roHkitonebHobwobqik50wbo5fkrwwonedzonefqorrbwtoit3q03ck5cvko5lzq3ktronedoHtbizvlHrkvdbrviowlo3wkdk9zonevoneldwwone9ic9q0ti3kwc5qH93wH5ofi9woneikord5oqlrzbiq5bH5vfvr0k9zzwiiltz33wrvH09lq3loctdb395zone5k5kdwoner09oneHoneo5vonebb5zvv00rblbv9vbt5onedHb0Honebczc53k5dcd9fwoor0klf3qonewonedz0Hl9btH9vltllrlqkivcwtwit9tzk5twtzonerdwonewbf5i9q9krwonef0wfcvilcvdqHbvodfoblllz9oneorwtzzov5vdht93zqf
Got:
bl9kittcrzk0qqqwrdrdwdrfdwtqroc05qbzkli0vkhb3frfqb3fl3wzr90ifbvtz005Htovv03wzwq9lfctcwfonekciwid5o3vtqz3dwHlv3illwv0roHkitonebHobwobqik50wbo5fkrwwonedzonefqorrbwtoit3q03ck5cvko5lzq3ktronedoHtbizvlHrkvdbrviowlo3wkdk9zonevoneldwwone9ic9q0ti3kwc5qH93wH5ofi9woneikord5oqlrzbiq5bH5vfvr0k9zzwiiltz33wrvH09lq3loctdb395zone5k5kdwoner09oneHoneo5vonebb5zvv00rblbv9vbt5onedHb0Honebczc53k5dcd9fwoor0klf3qonewonedz0Hl9btH9vltllrlqkivcwtwit9tzk5twtzonerdwonewbf5i9q9krwonef0wfcvilcvdqHbvodfoblllz9oneorwtzzov5vdht93zqf
'''