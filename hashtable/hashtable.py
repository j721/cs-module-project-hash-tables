class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

        #self.next node for linked list default value to none. To allow it to refer to another hash table entry
        #each entry is a key-value pair in the hash table


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here

        self.capacity = [None] * MIN_CAPACITY  #initialize array with 8 empty slots for hash table
        self.length = 0             #initialize length of the array to zero. that acts as counter


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
  
        return len(self.capacity)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

        #floor division method also works: return self.length//self.get_num_slots()
        # Divides and returns the integer value of the quotient. dumps the digits after the decimal.

        #number of items stored in the table/ total number of slots in the array
        return self.length/self.get_num_slots()


       


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

        hash = 5381

        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % len(self.capacity)

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here

        #self.capacity stands for hash table. getting the slot from the hash table
            #getting the key value from the slot in the hash table
             #reassigning that value to the new value that is being updated with the put
        # self.capacity[self.hash_index(key)] = value


        #put method stores value in a particular slot. Key-value pair
        i = self.hash_index(key)

        if self.capacity[i] is not None:  #if slot contains a key that is not None/empty  
            #if value is not None.      
            if self.capacity[i].value is not None:    
                current = self.capacity[i]              #set the current pointer to the first slot in the hash table
                self.capacity[i] = HashTableEntry(key,value)  #linking the class HashTableEntry and grabbing those values to link it
                self.capacity[i].next = current     #next pointer updated to our new current value

                #increment length
                self.length +=1                     #act as a counter to keep track of the updated value
                
                if self.get_load_factor() >= 0.7:           
                    self.resize(MIN_CAPACITY * 2)           #double the size of the hash table       
                return 

        self.capacity[i] = HashTableEntry(key, value)            #making it a linked list from calling HashTableEntry class
       
        self.length +=1                                       

        #check for load size
        if self.get_load_factor() >= 0.7:
            self.resize(MIN_CAPACITY * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

        # self.capacity[self.hash_index(key)] = None     
        
        #removing that value from key-value pair and set it to None

        #calling put method to grab the key, and the value be changed to None    
        self.put(key, None)    
        self.length -=1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        # return self.capacity[self.hash_index(key)]

        i = self.hash_index(key)            #index key-value pair 
        entry = self.capacity[i]            #index key-value pair at specific slot
    
        if entry is not None:
            while entry.next is not None:
                if entry.key == key:        #if key in the slot matches that the key that is wanting to be retrieved  return the value
                    return entry.value
                entry = entry.next

            return entry.value

        return None         #else if entry and next entry node is empty return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        global MIN_CAPACITY     #global keyword which allows to alter our global variable MIN_CAPACITY that was declared at the start
        MIN_CAPACITY = new_capacity         #reassign MIN_CAPACITY to new_capacity 

        current = self.capacity             #current variable for hash table

        self.capacity = [None] * MIN_CAPACITY       #initialize new hash table to be resized with 8 empty slots declared earlier 

        for x in current:       #for x in current hash table
            if (x is not None):     #if x element is not None and the x.next element is not None
                if (x.next is not None):
                     #have pointer point to next element in the list
                        pointer = x.next    
                         #pointer is on the new next element on the list, and is not None
                        while pointer is not None: 
                            # have it updated to the new key-value pair in the slot into the current/new hash table
                            self.put(pointer.key, pointer.value)
                            pointer = x.next #have pointer be assigned to the next node in the list
                self.put(x.key, x.value) #otherwise if there is no next node in the list, just update the key and value at the current slot



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")


    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")


