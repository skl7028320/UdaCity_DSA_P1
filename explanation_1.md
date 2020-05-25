# Problem 1 explanation
## Problem description
We are given total possible page numbers that can be referred. We are also given cache (or memory) size (Number of page 
frames that cache can hold at a time). The LRU caching scheme is to remove the least recently used frame when the cache 
is full and a new page is referenced which is not there in cache. Please see the Galvin book for more details. 

## Choice of data structure
Since all operations require O(1) time complexity, it's obvious that dictionary (HashMap) data structure which costs 
constant time for putting and getting element should be used to store data.

To handle the full capacity of LRU Cache, the used objects must be tracked so that the least recently used element can 
be deleted when the cache is full. Queue is a type of proper data structure to be used here because it is FIFO and the 
least recently used element will be near the tail (where deque happens) and the most recently used element will be near 
the head (where enqueue happens).

## Time complexity
For the costume `Queue` data structure, the input is the elements in the queue. Therefore the `enqueue()` and 
`dequeue()` costs constant time and the `move_node_to_tail()` has time complexity of O(n) because in worst case the 
queue needs to be fully traversed.

For the costume `Cache` class, the input is the elements in the cache. Since the `get()` calls `move_element_to_tail()` 
which costs O(n), it has time complexity of O(n). The `set()` only calls the deletion additionally which takes constant 
time and has time complexity of O(1).