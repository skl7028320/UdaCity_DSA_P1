class LinkedListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None       # where dequeue happens
        self.tail = self.head  # where enqueue happens
        self.num_elements = 0

    def enqueue(self, value):
        if self.head is None:
            self.head = LinkedListNode(value)
            self.tail = self.head
            self.num_elements = 1
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
            self.num_elements += 1

    def dequeue(self):
        if self.head is None:
            return None

        output_node = self.head
        self.head = self.head.next
        self.num_elements -= 1

        return output_node.value

    def move_node_to_tail(self, value):
        if self.head is None:
            return

        previous_node = None
        current_node = self.head
        while current_node:
            # find the target node at current node
            if value == current_node.value:
                # if the target node is not at the head
                if previous_node:
                    # if the target is already at the tail
                    if current_node.next is None:
                        return
                    previous_node.next = current_node.next
                    current_node.next = None
                    self.tail.next = current_node
                    self.tail = self.tail.next
                    return
                # if the target node is at the head
                else:
                    self.head = current_node.next
                    current_node.next = None
                    self.tail.next = current_node
                    self.tail = self.tail.next
                    return
            previous_node = current_node
            current_node = current_node.next

    def __repr__(self):
        visit_list = list()

        current_node = self.head
        while current_node:
            visit_list.append(current_node.value)
            current_node = current_node.next

        return visit_list

    def __str__(self):
        return str(self.__repr__())


class LRUCache:
    def __init__(self, capacity):
        self.cache = dict()
        self.capacity = capacity
        self.queue = Queue()

    def get(self, key):
        if self.capacity == 0:
            return "There is not any key-value structure in LRU cache because it has 0 capacity"
        if key in self.cache:
            self.queue.move_node_to_tail(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        if len(self.cache) == self.capacity:
            if self.capacity == 0:
                return "It's not possible to set any key-value structure because LRU cache capacity is 0."
            self._handle_full_capacity()
        self.cache[key] = value
        self.queue.enqueue(key)

    def _handle_full_capacity(self):
        key = self.queue.dequeue()
        del(self.cache[key])
        
    def __repr__(self):
        return self.cache
    
    def __str__(self):
        return str(self.__repr__())


# Test case 1
print("Test case 1:")
test_cache_1 = LRUCache(5)

print("Test set")
test_cache_1.set(1, 1)
test_cache_1.set(2, 2)
test_cache_1.set(3, 3)
test_cache_1.set(4, 4)
print("Pass" if str(test_cache_1) == "{1: 1, 2: 2, 3: 3, 4: 4}" else "Fail")

print("Test get")
print("Pass" if (test_cache_1.get(1) == 1) else "Fail")
print("Pass" if (test_cache_1.get(2) == 2) else "Fail")
print("Pass" if (test_cache_1.get(9) == -1) else "Fail")

print("Test full capacity handling")
test_cache_1.set(5, 5)
test_cache_1.set(6, 6)
print("Pass" if (test_cache_1.get(3) == -1) else "Fail")

# Test case 2
print("\nTest case 2:")
test_cache_2 = LRUCache(3)

print("Test set")
test_cache_2.set(1, 'a')
test_cache_2.set(2, 'b')
test_cache_2.set(3, 'c')
print("Pass" if str(test_cache_2) == "{1: 'a', 2: 'b', 3: 'c'}" else "Fail")

print("Test get")
print("Pass" if (test_cache_2.get(1) == 'a') else "Fail")
print("Pass" if (test_cache_2.get(2) == 'b') else "Fail")
print("Pass" if (test_cache_2.get(9) == -1) else "Fail")

print("Test full capacity handling")
test_cache_2.set(4, 'c')
print("Pass" if (test_cache_2.get(3) == -1) else "Fail")

# Test case 3
print("\nTest case 3:")
test_cache_3 = LRUCache(0)

print("Test set")
'''
When the capacity of LRU cache is 0, it's not possible to insert any element into cache. Practically an assertion error
should be raised but here a string is returned instead for test purpose.
'''
print("Pass" if test_cache_3.set(1, 1) == "It's not possible to set any key-value structure because LRU cache capacity "
                                          "is 0."
      else "Fail")

print("Test get")
'''
When the capacity of LRU cache is 0, it's not possible to get any element from cache. Practically an assertion error
should be raised but here a string is returned instead for test purpose.
'''
print("Pass" if test_cache_3.get(1) == "There is not any key-value structure in LRU cache because it has 0 capacity"
      else "Fail")
