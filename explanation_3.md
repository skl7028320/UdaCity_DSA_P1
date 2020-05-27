# Problem 3 explanation
## Problem description
In general, a data compression algorithm reduces the amount of memory (bits) required to represent a message (data). 
The compressed data, in turn, helps to reduce the transmission time from a sender to receiver. The sender encodes the 
data, and the receiver decodes the encoded data. As part of this problem, you have to implement the logic for both 
encoding and decoding.

A data compression algorithm could be either lossy or lossless, meaning that when compressing the data, there is a loss 
(lossy) or no loss (lossless) of information. The **Huffman Coding** is a lossless data compression algorithm. It 
comprises of two phases - **Encodeing** and **Decoding**.

## Solution
For the encoding part, the pipeline is **build priority queue** -> **build huffman tree** -> **generate char code** -> 
**create encoded data**. For the decoding part, The encoded data is used as guide to traverse the generated Huffman 
tree to recover the original data.

The basic 'Node' class is used for both priority queue and Huffman tree. Priority queue is implemented by linked list.

## Time complexity
For `build_priority_queue()`, every time a new character is inserted into the priority queue, the priority queue needs 
be completely traversed in worst case. Assuming the number of input character is n, the time complexity is O(n^2). 
`build_huffman_tree()` has O(n) time complexity because the priority queue needs to dequeue all elements and insert 
them into Huffman tree. `generate_char_code()` traverses the Huffman tree. Therefore it has the time complexity of 
O(h) where n is the number of elements in Huffman tree. `create_encoded_data()` takes O(n) where n is the size of 
string. Hence, the overall time complexity of Huffman encoding part is O(n^2) because all the procedures can be 
neglected other than building the priority queue.

For decoding part of Huffman coding, the time complexity is simply O(n) where n is the number of bits in encoded data 
as well as the width of Huffman tree.