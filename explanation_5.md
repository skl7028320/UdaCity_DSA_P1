# Problem 5 explanation
## Problem description
A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how 
it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous 
block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time 
when the block was created, and text strings as the data.

## Solution
Blockchain is notion more but a linked list where blocks are nodes and they are connected by storing reference to next 
node in current node.

## Time complexity
Appending a block to blockchain has time complexity of O(1) just like normal linked list by adding element to the head 
side of blockchain.

## Space complexity
For appending block to blockchain, the space complexity is O(n) because it's only simply linking the new block to the 
current head of blockchain and no extra space is used. For calculating hash, a new string comprising all information in 
block and a `sha256` object is created. Therefore the space complexity is O(n) where n is the number of block inserted 
into blockchain.