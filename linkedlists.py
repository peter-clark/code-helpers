## LINKED LISTS ##

# Singly Linked List
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    ### Recursively go through list and sum ###
    # You are given two non-empty linked lists representing 
    # two non-negative integers. The digits are stored in 
    # *reverse order*, and each of their nodes contains 
    # a single digit. Add the two numbers and 
    # return the sum as a linked list.
    def TraverseListWithSum(self, li, sum, depth): 
        if li is None:
            return sum
        
        # your desired operation to recurse here
        # print(depth)
        sum += li.val * (10 ** depth)
        depth += 1
        return self.TravList(li.next, sum, depth)