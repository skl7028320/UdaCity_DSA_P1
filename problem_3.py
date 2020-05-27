import sys
from collections import deque


class Node:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.next = None
        self.left = None
        self.right = None

    def has_left_child(self):
        if self.left is None:
            return False
        else:
            return True

    def get_left_child(self):
        return self.left

    def has_right_child(self):
        if self.right is None:
            return False
        else:
            return True

    def get_right_child(self):
        return self.right

    def __str__(self):
        return f"Node({self.char}, {self.frequency})"


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    '''
    The function is used to insert a new node into the queue
    at a proper position based on the priority of the node
    '''
    def enqueue(self, new_node):
        if self.is_empty():
            self.head = new_node
            self.num_elements = 1

            return

        current_node = self.head
        previous_node = None
        while current_node:
            if new_node.frequency > current_node.frequency:
                if current_node.next is None:
                    current_node.next = new_node
                    self.num_elements += 1
                    break
                previous_node = current_node
                current_node = current_node.next
            else:
                if previous_node is None:
                    new_node.next = self.head
                    self.head = new_node
                    self.num_elements += 1
                    break
                new_node.next = current_node
                previous_node.next = new_node
                self.num_elements += 1
                break

    '''
    The function is used to removes the element with the
    lowest priority from the queue
    '''
    def dequeue(self):
        if self.is_empty():
            return None

        output_node = self.head
        self.head = self.head.next
        self.num_elements -= 1

        return output_node

    '''
    The function is used to get the lowest priority element
    in the queue without removing it from the queue
    '''
    def top(self):
        return self.head

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def convert_to_list(self):
        repr_list = list()

        current_node = self.head
        while current_node:
            repr_list.append((current_node.char, current_node.frequency))
            current_node = current_node.next

        return repr_list


print("Test priority queue:")
test_queue = PriorityQueue()
test_node = Node('a', 1)
test_queue.enqueue(test_node)
test_node = Node('c', 3)
test_queue.enqueue(test_node)
test_node = Node('b', 2)
test_queue.enqueue(test_node)
test_node = Node('e', 5)
test_queue.enqueue(test_node)
test_node = Node('d', 4)
test_queue.enqueue(test_node)
print("Pass\n" if test_queue.convert_to_list() == [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)] else "Fail\n")


def build_priority_queue(data):
    queue = PriorityQueue()
    count = 0
    current_char = data[0]
    for i, char in enumerate(data):
        if char == current_char:
            count += 1
            if i == len(data) - 1:
                node = Node(current_char, count)
                queue.enqueue(node)
                continue
        else:
            node = Node(current_char, count)
            queue.enqueue(node)
            if i == len(data) - 1:
                node = Node(char, 1)
                queue.enqueue(node)
                continue
            current_char = char
            count = 1

    return queue


print("Test build_priority_queue()")
test_data = "AAAAAAABBBCCCCCCCDDEEEEEE"
test_queue = build_priority_queue(test_data)
print("Pass\n" if test_queue.convert_to_list() == [('D', 2), ('B', 3), ('E', 6), ('C', 7), ('A', 7)] else "Fail\n")


class Queue:
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)


class HuffManTree:
    def __init__(self, node=None):
        self.root = node

    def get_root(self):
        return self.root

    def __repr__(self):
        level = 0
        visit_order = list()
        q = Queue()
        q.enq((self.get_root(), level))

        while len(q) > 0:
            node, level = q.deq()
            if node is None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append(((node.char, node.frequency), level))

            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_left_child:
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Huffman Tree"
        previous_level = -1

        for i in range(len(visit_order)):
            node, level = visit_order[i]

            if level == previous_level:
                s += " | " + str(node)
            elif level > previous_level:
                s += "\n" + str(node)
                previous_level = level

        return s


def build_huffman_tree(queue):
    while queue.size() > 1:
        low_priority_node = queue.dequeue()
        high_priority_node = queue.dequeue()
        new_node = Node(None, low_priority_node.frequency + high_priority_node.frequency)
        new_node.left = low_priority_node
        new_node.right = high_priority_node
        queue.enqueue(new_node)

    return HuffManTree(queue.dequeue())


print("Test build_huffman_tree()")
test_tree = build_huffman_tree(test_queue)
print(str(test_tree) + "\n")


def generate_char_code(tree):
    look_up_table = dict()

    def traverse(node, code):
        if node.has_left_child():
            new_code = code + "0"
            traverse(node.get_left_child(), new_code)
        if node.has_right_child():
            new_code = code + "1"
            traverse(node.get_right_child(), new_code)
        if not node.has_left_child() and not node.has_right_child():
            look_up_table[node.char] = code

    root = tree.get_root()
    empty_code = str()
    traverse(root, empty_code)

    return look_up_table


print("Test generate_char_code()")
test_look_up_table = generate_char_code(test_tree)
print("Pass\n" if test_look_up_table == {'D': '000', 'B': '001', 'E': '01', 'C': '10', 'A': '11'} else "Fail\n")


def create_encoded_data(data, look_up_table):
    encoded_data = str()

    for char in data:
        encoded_data += look_up_table[char]

    return encoded_data


print("Test create_encoded_data()")
test_encoded_data = create_encoded_data(test_data, test_look_up_table)
print("Pass" if test_encoded_data == "1111111111111100100100110101010101010000000010101010101" else "Fail")


def huffman_encoding(data):
    queue = build_priority_queue(data)
    tree = build_huffman_tree(queue)
    look_up_table = generate_char_code(tree)
    encoded_data = create_encoded_data(data, look_up_table)
    return encoded_data, tree


def huffman_decoding(data, tree):
    decoded_data = str()
    current_node = tree.get_root()
    
    for i in range(len(data)):
        if '0' == data[i]:
            current_node = current_node.left
        elif '1' == data[i]:
            current_node = current_node.right

        if not current_node.has_left_child() and not current_node.has_right_child():
            decoded_data += current_node.char
            current_node = tree.get_root()

    return decoded_data


if __name__ == "__main__":
    print(f"""
-------------------------------------------------------------
Main function starts here
""")

    print(f"""---------------------------------------
Test case 1: 
""")
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))

    print(f"""---------------------------------------
Test case 2: 
    """)
    a_great_sentence = "Time is gold"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))

    print(f"""---------------------------------------
Test case 3: 
    """)
    a_great_sentence = "valar morghulis"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))
