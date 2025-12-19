# Roll a dice 10 times using random.randint() and counts] how many times you get 6
import random
def dice():
        count = 0
        for i in range(10):
            r = random.randint(1,6)
            print("Roll:",r)
            if r == 6:
                count +=1
            return count
print("Six came:", dice(),"times")