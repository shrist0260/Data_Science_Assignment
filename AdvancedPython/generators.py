# 3. Create a generator that yields numbers from 1 to 5 one by one. (generators)

def nums (n):
    for i in range(1, n+1):
        yield i
    
for num in nums(5):
    print(nums)