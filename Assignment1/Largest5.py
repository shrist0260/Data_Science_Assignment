# write a program that asks for five number and prints the largest using a function
def largest(arr_):
    max_num = arr_[0]   
    for a in arr_:
        if a>max_num:
            max_num =a
        return max_num
largest([1,2,3,4,2])