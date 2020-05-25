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


# test_queue = Queue()
# test_queue.enqueue(1)
# test_queue.enqueue(2)
# test_queue.enqueue(3)
# test_queue.enqueue(4)
# test_queue.enqueue(5)
# print("Test enqueue")
# print(str(test_queue))
# output_value = test_queue.dequeue()
# print("Test dequeue")
# print("Output value is: {}".format(output_value))
# print(test_queue)
# test_queue.move_node_to_tail(7)
# print("Test move_node_to_tail with non-existing value")
# print(test_queue)
# test_queue.move_node_to_tail(2)
# print("Test move_node_to_tail with existing value")
# print(test_queue)


class LRUCache:
    def __init__(self, capacity):
        self.cache = dict()
        self.capacity = capacity
        self.queue = Queue()

    def get(self, key):
        if key in self.cache:
            self.queue.move_node_to_tail(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        if len(self.cache) == self.capacity:
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


# test_cache = LRUCache(5)
# print("Test creation of cache")
# print(test_cache)
#
# test_cache.set(1, 1)
# test_cache.set(2, 2)
# test_cache.set(3, 3)
# test_cache.set(4, 4)
# print("Test set")
# print(test_cache)
#
# print("Test get")
# print(test_cache.get(1))       # returns 1
# print(test_cache.get(2))       # returns 2
# print(test_cache.get(9))       # returns -1 because 9 is not present in the cache
#
# print("Test full capacity handling")
# test_cache.set(5, 5)
# test_cache.set(6, 6)
# print(test_cache.get(3))       # returns -1 because 3 is deleted from cache
# print(test_cache)
