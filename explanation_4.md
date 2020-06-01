# Problem 4 explanation
## Problem description
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as 
such. Where User is represented by str representing their ids. Write a function that provides an efficient look up of 
whether the user is in a group.

## Solution
Since a group can contain another group, the problem can be solved recursively. The recursion function is designed in 
such way that it takes the queried user name and the searching group as input and returns True if the user is found and 
false otherwise.

## Time complexity
In the worst case that the user is not in the group, the whole tree structure is traversed and therefore the time 
complexity is O(n) where n is the number of elements in the tree including internal and external nodes.

## Space complexity
The space complexity is O(n) because for each element in the group, there is a bool value created.