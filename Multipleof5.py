#Print a multiplicationtable for a number, but highlight multiple of 5

num = int(input("Number"))
print(f"Multiplication table for {num}:")

for i in range(1, 11): 
    result = num * i 
    # highlight multiple of 5 
    if result%5 == 0: 
        print(f"{num} * {i}={result}") 
    else: 
        print(f"{num} * {i}={result}")
