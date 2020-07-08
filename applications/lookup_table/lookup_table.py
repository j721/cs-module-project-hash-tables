# Your code here


#make imports from libraries
import math
import random

#create a cache dictionary globally
cache ={}

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    
    def slowfun_cache(x,y):
        v = math.pow(x, y)
        #if the value is not in the cache, perform operations and add it to the cache
        if v not in cache:
            cache[v] = math.factorial(v)
            cache[v] //= (x + y)
            v %= 982451653
        print(v)
        return(v)
    #if value not in cache then just return it
    return slowfun_cache(x,y)


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
