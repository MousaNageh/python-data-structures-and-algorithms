
class Node:
    
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right
        
    
    def __str__(self) -> str:
        return str(self.value)
    

class BinarySearchTree:
    
    def __init__(self) -> None:
        self.root: Node = None  
        self.size =  0 
        
    # O(log n)
    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node 
        else:
            current = self.root
            while current:
                # left 
                if value < current.value:
                     # insert id not nodes not exist on the right 
                    if current.left is None:
                        current.left = new_node 
                        break 
                    else:
                        # go left 
                        current = current.left 
                # right 
                else:
                    # insert id not nodes not exist on the right 
                    if current.right is None:
                        current.right = new_node 
                        break 
                    else:
                        # go right 
                        current = current.right 
        self.size += 1 
    
    
    def remove(self, value):
        if not self.root:
            return False
        current = self.root 
        parent = None 
        is_left_node = False 
        # whe need the following 
        # 1 - find node 
        # 2 - find parent node 
        # 3 - determine if the node is left node or right node 
        
        # find the target and and determine if is a left node or right node 
        while current and current.value != value:
            parent = current
            # go left 
            if value < current.value:
                is_left_node = True 
                current = current.left 
            # go right 
            else:
                current = current.right 
                is_left_node = False 
    
        # value not founded in the tree 
        if not current:
            return False
                
        # case 1 : if the target node has no children
        if current.left is None and current.right is None:
            # if the target node is the root , then the tree contains only one node which is the root
            if not parent:     
                self.root = None 
            # if target node is left node for parent, make the left of the parent null 
            elif is_left_node:     
                parent.left = None 
            # if target node is right node for parent, make the right of the parent null 
            else:
                parent.right = None
        
        # case 2 : if the target node has only left node 
        elif current.left and current.right is None:
            # if the target node is the root , then make the root points to the left of the current node
            if not parent:     
                self.root = current.left 
            # if the target node is left node , make the parent points to the left of the target node
            elif is_left_node:
                parent.left = current.left  
            
            # if the target node is left node, make the parent points to the left of the target node
            else:
                parent.right = current.left
        
        # case 3 : if the target node has only right node 
        elif current.right and current.left is None:
            # if the target node is the root , then make the root points to the right of the current node
            if not parent:     
                self.root = current.right 
            # if the target node is left node , make the parent points to the right of the target node
            elif is_left_node:
                parent.left = current.right  
            
            # if the target node is right node, make the parent points to the right of the target node
            else:
                parent.right = current.right    
        
        
        # Case 3: The target node  has two children.
        else: 
            # Find the in-order successor (smallest value in the right subtree)
            successor: Node = current.right
            successor_parent: Node  = current
            while successor.left:
                successor_parent = successor
                successor = successor.left
            
            # Replace current node with successor value.
            current.value = successor.value      
            
            # Fix the successor's parent's child reference.
            if successor_parent == current:  # Successor was the direct right child.
                successor_parent.right = successor.right
            else:  # Successor was not the direct right child.
                successor_parent.left = successor.right
        
        self.size -= 1
        return True
                    
    # O(log n) if a balanced tree, O(n) if unbalanced tree 
    def search(self, value):
        current = self.root 
        while current:
            if current.value == value:
                return True 
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False
    
    # O(n)
    def depth(self):
        max_depth = 0
        if self.root:  
            queue = [(self.root, 1)]
            while queue:
                current, depth = queue.pop(0)
                if depth > max_depth:
                    max_depth = depth 
                
                if current.left:
                    queue.append((current.left, depth + 1))
                if current.right:
                    queue.append((current.right, depth + 1))
        return max_depth
         
   
    def in_order(self):
        cur = self.root 
        self._in_order(cur)
        
    # left - middle - right  (print at middle or return at middle)
    @classmethod
    def _in_order(cls, root: Node):
        if root:
            cls._in_order(root.left)
            print(root.value, end=' ')
            cls._in_order(root.right)
    
    def pre_order(self):
        cur = self.root 
        self._pre_order(cur)
        
    # middle  - left - right (print at middle or return at begin)
    @classmethod
    def _pre_order(cls, root: Node):
        if root:
            print(root.value, end=' ')
            cls._pre_order(root.left)
            cls._pre_order(root.right)
    
    def post_order(self):
        cur = self.root 
        self._pre_order(cur)
        
    # left - right - middle (print at middle or return at last)
    @classmethod
    def _post_order(cls, root: Node):
        if root:
            cls._post_order(root.left)
            cls._post_order(root.right)
            print(root.value, end=' ')
            

t = BinarySearchTree()
t.insert(10)
t.insert(21)
t.insert(7)

