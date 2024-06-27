# Exercise 1 -----------------------------------------------------------------
class Node:
    pos: int = 0

    def __init__(self, val: list, next: "Node" = None) -> None:
        self.val: list = val
        self.next: Node = next
        self.pos: int = Node.pos
        
        Node.pos += 1

class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None

    def append(self, val: int):

        # If the head Node is empty, set the given value as a Node
        if not self.head:
            self.head = Node(val)

        # Else scrolls through the Node until it finds the last one
        else:
            current = self.head
            while current.next:
                current = current.next

            # Once find the last Node append the value as the new last Node
            current.next = Node(val)

    def get_node(self, val: int) -> Node:

        # Initialize the first 'linkedList' 'Node' as 'current' 
        current = self.head

        # Scroll through the 'linkedList' Nodes until it find the Node with the given value
        while current.val != val:
            current = current.next
        
        # Return the node with the given value
        return current


def has_cycle(head: Node) -> list[int]:
        
    node_pos: list[int] = []
        
    # Initialize the given 'Node' as 'current' 
    current = head

    # Scroll through the 'Node' next Nodes until it finds a cycle
    while True:

        # If the current 'Node' is the last of the 'linkedList', return False
        if current.next == None:
            return False

        # If the 'Node' pos is in the 'node_pos' list, return True
        elif current.pos in node_pos:
            return True
        
        # If the 'Node' pos is not in the scrolled Node pos list, append it
        else:
            node_pos.append(current.pos)
        
        # Go to the next 'Node'
        current = current.next


ll2 = LinkedList()
for i in range(5):
    ll2.append(i)

print(has_cycle(ll2.head))
# ----------------------------------------------------------------------------



# Exercise 2 -----------------------------------------------------------------
class Queue:
    
    def __init__(self) -> None:
        self.queue: list = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> None:
        return self.queue.pop(0)

    def top(self) -> int:
        return self.queue[0]
    
    def empty(self) -> bool:

        if len(self.queue) == 0:
            return True
        
        else:
            return False


class MyStack:
    
    def __init__(self) -> None:
        self.queue: Queue = Queue()
        self.temp: Queue = Queue()

    def push(self, x: int) -> None:
        self.queue.push(x)

    def pop(self) -> None:
        while not self.queue.empty():
            popped_q = self.queue.pop()
            if not self.queue.empty():
                self.temp.push(popped_q)

        while not self.temp.empty():
            popped_t = self.temp.pop()
            self.queue.push(popped_t)

        return popped_q

    def top(self) -> int:
        while not self.queue.empty():
            popped_q = self.queue.pop()
            self.temp.push(popped_q)

        while not self.temp.empty():
            popped_t = self.temp.pop()
            self.queue.push(popped_t)

        return popped_q
    
    def empty(self) -> bool:
        return self.queue.empty()
# ----------------------------------------------------------------------------



# Exercise 3 -----------------------------------------------------------------
class LinkedList:
    pass
        
def is_palindrome(head: Node) -> list[int]:
    pass
# ----------------------------------------------------------------------------



# Exercise 4 -----------------------------------------------------------------
def is_valid_parenthesis(s: str) -> bool:

    # Initialize needed variables
    parenthesis = []
    parenthesis_mapping = {')': '(', '}': '{', ']': '['}
    
    # Iterate in the string
    for char in s:

        # If a parenthesis get opened, store it
        if char in parenthesis_mapping.values():
            parenthesis.append(char)

        # If a parenthesis got closed, check for validity
        elif char in parenthesis_mapping.keys():

            # In case of parenthesis closed but not opened, return False
            if parenthesis == []:
                return False
            
            # If closed parenthesis do not corresponds to open parenthesis, return False
            elif parenthesis_mapping[char] != parenthesis.pop():
                return False
        
        # In case of non parenthesis, return False
        else:
            return False
            
    
    # If all parenthesis has been closed correctly, return True
    return parenthesis == []     
# ----------------------------------------------------------------------------



# Exercise 5 -----------------------------------------------------------------
def longest_palindrome(s: str) -> int:

    # Initialize a dict where to store each char occurence data
    char_occurrences: dict[str, int] = {}
    
    # Count occurences for each char
    for char in s:
        if char in char_occurrences:
            char_occurrences[char] += 1
        else:
            char_occurrences[char] = 1
    
    # Initialize need variables
    longest_palindrome_length = 0
    odd_lenght = False
    
    # Count the lenght of the longest possible palindrome word
    for count in char_occurrences.values():

        if count % 2 == 0:
            longest_palindrome_length += count

        # Can handle single occurence and odd occurences of a char
        else:
            longest_palindrome_length += count - 1
            odd_lenght = True
    
    if odd_lenght:
        longest_palindrome_length += 1
    
    return longest_palindrome_length
        
        


# ----------------------------------------------------------------------------



# Exercise 6 -----------------------------------------------------------------
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:

    # Determinates the last x elements of 'nums1' that are usless
    usless: int = len(nums1) - m

    if usless > 0:
        # Remove useless numbers from 'nums1'
        del nums1[-usless:]

    # Append all 'nums2' numbers to 'nums1'
    nums1.extend(nums2)

    # Sort 'nums1' numbers in non-decrasing order
    nums1.sort()
# ----------------------------------------------------------------------------