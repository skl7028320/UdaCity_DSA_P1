# Problem 6 explanation
## Problem description
Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the 
set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is 
the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, 
respectively. Once you have completed the problem you will create your own test cases and perform your own run time 
analysis on the code.

## Solution
By finding the same elements in list A and B and exclude them from output list or insert them into output list, the 
union or intersection of two lists can be obtained respectively. Therefore the main idea is loop through both lists in 
order to find the same nodes.

## Run time analysis
For union function, first the list A is traversed and for each element in list A the list B is traversed to find the 
same element. Here the time complexity is O(m * n) where m is the size of list A and n is the size of list B. 
Meanwhile, the found same element is inserted into output list. Then all the elements in list B are inserted into 
output list by traversing them, which takes time complexity of O(n). In summary, the overall time complexity is 
O(m * n + n) where O(n) is negligible when m is not much smaller than n resulting final time complexity O(m * n).

For intersection function, the analogous operation is executed to find the same elements in list A and B. The 
difference is that only the same elements are inserted into output list. Therefore the time complexity is O(m * n)