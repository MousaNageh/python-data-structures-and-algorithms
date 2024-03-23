'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Input: head = [1,1,1,2,3]
Output: [2,3]

'''

def delete_duplicates(head):

    if not head or not head.next:
        return head 

    duplicate_values ={}
    current = head 
    while current:
        if  duplicate_values.get(current.val) is None:
            duplicate_values[current.val] = 0 
        else:
            duplicate_values[current.val] = duplicate_values[current.val] + 1
        current = current.next 
    
    current = head 
    prev = None 
    while current:
        if duplicate_values[current.val] > 0:
            if not prev:
                head = head.next
                current = head
            else:
                prev.next = current.next 
                current = current.next 
        else:
            prev = current 
            current = current.next 
    return head