# Your code here


"""
Hint: In Python, a dict key can be any immutable type... including a
tuple.

In Python, there are two objects that correspond to hash tables, dict and set. 
A dict is a special kind of hash table called an associative array. 
An associative array is a hash table where each element of the hash table points to another object. 
The other object itself is not hashed

`x`, `y`, and `z` are all >= zero.

"""

#maybe create a cache dictionary again?

cache ={}

def expensive_seq(x, y, z):
    # Your code here

    # if variables found in cache then just return the cache with those values
    if (x, y, z) in cache:
        return cache[x, y, z]

    if x <= 0: return y + z

    if x >  0: 
        value = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
        #add the new computed values into cache
        cache[x,y,z] = value
        #return the new updated value
        return value


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
