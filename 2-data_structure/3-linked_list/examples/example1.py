# rotate  linked list k to right times 

#  Input: head = [1,2,3,4,5], k = 2
#  Output: [4,5,1,2,3]

# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

# Constraints:

#The number of nodes in the list is in the range [0, 500].
#  -100 <= Node.val <= 100
#   0 <= k <= 2 * 109

def rotate_right(head, k):
    if not head or not head.next or k == 0:
        return head
    
    # Step 1: Calculate the length of the list and make it circular.
    
    length = 1
    current = head
    while current.next:
        current = current.next  
        length += 1
    
    # Make the list circular
    current.next = head
    
    # Step 2: Calculate the effective rotations needed.
    k = k % length
    steps_to_new_head = length - k
    
    # Step 3: Find the new head.
    new_tail = head
    for _ in range(steps_to_new_head - 1):
        new_tail = new_tail.next
    
    new_head = new_tail.next
    
    # Step 4: Break the circle.
    new_tail.next = None
    
    return new_head