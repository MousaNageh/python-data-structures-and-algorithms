#Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying 
# the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

# Input: head = []
# Output: []

# Input: head = [1]
# Output: [1]

def swap_pairs(head):
    if not head or not head.next:
        return head
    cur = head
    while cur and cur.next:
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next 
    return head