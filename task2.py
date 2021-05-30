stringToSort = input("Enter a random string: ")





def my_sort(string):

    result = ""
    all_chars = len(string)
    for i in range(all_chars):

        minimum = ""

        for j in range(len(string)):

            if minimum == "" or minimum > string[j]:
                minimum = string[j]

        result += minimum
        string = string.replace(minimum, "", 1)


    return result


    
print(my_sort(stringToSort))



