# 2. Create a list of even numbers only from 1 to 20. (list comprehension)

squares = [x*x for x in range(1, 8)]
print(squares)

even_num=[i for i in range(1, 21) if i %2 == 0]
print(even_num)
