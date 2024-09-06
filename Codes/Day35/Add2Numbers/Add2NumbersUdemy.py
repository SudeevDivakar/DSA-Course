class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addAtTail(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return self

def add2Numbers(l1, l2):
    #write your code here
    num1 = l1
    num2 = l2
    carry = 0
    sum_linked_list = LinkedList()
    
    while num1 != None or num2 != None:
        if num1 and num2:
            addition = num1.value + num2.value + carry
            digit = addition % 10
            carry = addition // 10
            sum_linked_list.addAtTail(digit)
            num1 = num1.next
            num2 = num2.next
            
        elif num1 and not num2:
            addition = num1.value + carry
            digit = addition % 10
            carry = addition // 10
            sum_linked_list.addAtTail(digit)
            num1 = num1.next
            
        elif not num1 and num2:
            addition = num2.value + carry
            digit = addition % 10
            carry = addition // 10
            sum_linked_list.addAtTail(digit)
            num2 = num2.next
            
    if carry > 0:
        sum_linked_list.addAtTail(carry)
        
    return sum_linked_list

# Time Complexity = O(max(m, n))       where m is length of first linked list and n is length of second linked list
# Space Complexity = O(max(m, n))      according to Udemy and Leetcode, but I feel like it should be O(1) cuz output linked list does not count as auxiliary space