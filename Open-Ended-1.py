# Name: Syed Shahriyar Ali
# Roll No: 22F-BSAI-06

class Node:
  def __init__(self, value=0, next=None):
    self.value = value
    self.next = next

def reverse_linked_list(head: Node) -> Node:
    stack = []

    currentNode = head

    while currentNode != None:
       stack.append(currentNode.value)
       currentNode = currentNode.next

    reversed = Node()
    currentNode = reversed

    for _ in range(len(stack)):
        currentNode.value = stack.pop()
        
        if len(stack) > 0:
            currentNode.next = Node()
        
        currentNode = currentNode.next
        
    return reversed

def print_linked_list(head: Node):
    while head != None:
        print(head.value)
        head = head.next

# Initialize a Linked List

head = Node(1)
currentNode = head

for i in range(2, 6):
    currentNode.next = Node(i)
    currentNode = currentNode.next

# Print Linked List Before Reverse
print("=== Linked List Before Reversed ===", end="\n")
print_linked_list(head)

# Reverse the Linked List
head = reverse_linked_list(head)

# Print the Linked List After Reverse
print("=== Linked List After Reversed ===", end="\n")
print_linked_list(head)