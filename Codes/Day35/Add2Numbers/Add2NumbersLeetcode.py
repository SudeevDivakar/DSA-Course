# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = l1
        num2 = l2
        carry = 0
        sum_list = None
        current = None

        while num1 != None or num2 != None:
            if num1 and num2:
                addition = num1.val + num2.val + carry
                carry = addition // 10
                digit = addition % 10
                if not sum_list:
                    sum_list = ListNode(digit)
                    current = sum_list
                else:
                    new_node = ListNode(digit)
                    current.next = new_node
                    current = current.next
                num1 = num1.next
                num2 = num2.next
            
            elif num1 and not num2:
                addition = num1.val + carry
                digit = addition % 10
                carry = addition // 10

                new_node = ListNode(digit)
                current.next = new_node
                current = current.next

                num1 = num1.next
                
            elif not num1 and num2:
                addition = num2.val + carry
                digit = addition % 10
                carry = addition // 10

                new_node = ListNode(digit)
                current.next = new_node
                current = current.next

                num2 = num2.next

        if carry > 0:
            new_node = ListNode(carry)
            current.next = new_node

        return sum_list


# Time Complexity = O(max(m, n))       where m is length of first linked list and n is length of second linked list
# Space Complexity = O(max(m, n))      according to Udemy and Leetcode, but I feel like it should be O(1) cuz output linked list does not count as auxiliary space