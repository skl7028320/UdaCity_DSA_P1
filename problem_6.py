class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.num_elements = 1
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.num_elements += 1

    def is_empty(self):
        return self.num_elements == 0

    def size(self):
        return self.num_elements

    def __repr__(self):
        output_str = ""

        current_node = self.head
        while current_node:
            if current_node.next:
                output_str += str(current_node.value) + " <- "
            else:
                output_str += str(current_node.value)

            current_node = current_node.next

        return output_str


def union(llist_1, llist_2):
    output_llist = LinkedList()

    # Handle extreme cases
    if llist_1.is_empty():
        return llist_2
    if llist_2.is_empty():
        return llist_1
    if llist_1.is_empty() and llist_2.is_empty():
        return output_llist

    # Find elements that are in list 1 but not in list 2 and put them into output list
    current_node_1 = llist_1.head
    while current_node_1:
        find_same_node = False

        current_node_2 = llist_2.head
        while current_node_2:
            if current_node_1.value == current_node_2.value:
                find_same_node = True
                break
            current_node_2 = current_node_2.next

        if not find_same_node:
            output_llist.append(current_node_1.value)

        current_node_1 = current_node_1.next

    # Put elements of list 2 into output list
    current_node_2 = llist_2.head
    while current_node_2:
        output_llist.append(current_node_2.value)
        current_node_2 = current_node_2.next

    return output_llist


def intersection(llist_1, llist_2):
    output_llist = LinkedList()

    # Handle extreme case
    if llist_1.is_empty() or llist_2.is_empty():
        return output_llist

    # Find elements that are in list 1 and in list 2 and put them into output list
    current_node_1 = llist_1.head
    while current_node_1:
        find_same_node = False

        current_node_2 = llist_2.head
        while current_node_2:
            if current_node_1.value == current_node_2.value:
                find_same_node = True
                break
            current_node_2 = current_node_2.next

        if find_same_node:
            output_llist.append(current_node_1.value)

        current_node_1 = current_node_1.next

    return output_llist


# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in element_2:
    linked_list_2.append(i)

print("Test case of one empty list")
print("Pass" if str(union(linked_list_1,linked_list_2)) == "9 <- 8 <- 7 <- 6 <- 5 <- 4 <- 3 <- 2 <- 1" else "Fail")
print("Pass" if str(intersection(linked_list_1,linked_list_2)) == "" else "Fail")

# Test case 2
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("Test case of two identical linked lists")
print("Pass" if str(union(linked_list_1,linked_list_2)) == str(intersection(linked_list_1, linked_list_2)) else "Fail")

# Test case 3
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1, 3, 5, 7, 9]
element_2 = [2, 4, 6, 8]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("Test case of two non-intersected lists")
print("Pass" if str(union(linked_list_1,linked_list_2)) == "2 <- 4 <- 6 <- 8 <- 1 <- 3 <- 5 <- 7 <- 9" else "Fail")
print("Pass" if str(intersection(linked_list_1,linked_list_2)) == "" else "Fail")

# Test case 4
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [4, 1, 2, 7, 9, 25, 68]
element_2 = [68, 4, 5, 8, 27, 7]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("Test case of two lists having both intersection and non-intersection")
print("Pass" if str(union(linked_list_1,linked_list_2)) == "68 <- 4 <- 5 <- 8 <- 27 <- 7 <- 1 <- 2 <- 9 <- 25" else "Fail")
print("Pass" if str(intersection(linked_list_1,linked_list_2)) == "4 <- 7 <- 68" else "Fail")
