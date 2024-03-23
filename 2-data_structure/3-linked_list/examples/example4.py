'''
Given the head of a sorted linked list, 
delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Input: head = [1,1,2]
Output: [1,2]

Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''


def delete_duplicates(head):
    my_dict = {} 
    currrent = head 
    prev = None
    while currrent:
        if my_dict.get(currrent.val):
            prev.next = currrent.next
        else:
            my_dict[currrent.val] = True
            prev = currrent 
        currrent = currrent.next
    return head