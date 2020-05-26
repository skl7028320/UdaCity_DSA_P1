# Problem 2 explanation
## Problem description
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) 
that end with ".c".

## Solution
The problem can be solved by using recursion. The required files in current directory can be found by finding the 
required files in the subdirectories of current directory. This forms a recursion and the base case is that the input 
is already a file. When the input file has the desired suffix, return the file as a list. Otherwise return an empty 
list. By appending all the small output returned by recursion the final output is obtained and returned.

## Time complexity
The input of function is a directory which is essentially a tree data structure. In order to find the required file the 
tree needs to be completely traversed. Therefore the time complexity is O(n).