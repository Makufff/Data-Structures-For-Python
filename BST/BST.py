# Node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST :
    # init
    def __init__(self):
        self.root = None

    # Insertion (interative)
    def insert_interative(self, value):
        new_node = Node(value)
        
        # if the tree is empty
        if self.root == None :
            self.root = new_node
            return
        
        # if the tree is not empty
        current_node = self.root
        while True :
            if new_node.value < current_node.value :
                if current_node.left == None:
                    current_node.left = new_node
                    returnx
                current_node = current_node.left
            else :
                if current_node.right == None:
                    current_node.right = new_node
                    return
                current_node = current_node.right

    # Insertion (recursive) # addon
    def insert_recursive_helper(self, current_node, new_node):
        if new_node.value < current_node.value :
            if current_node.left == None :
                current_node.left = new_node
                return
            self.insert_recursive_helper(current_node.left, new_node)
        else :
            if current_node.right == None :
                current_node.right = new_node
                return
            self.insert_recursive_helper(current_node.right, new_node)

    def insert_recursive(self, value):
        new_node = Node(value)
        # if the tree is empty
        if self.root == None :
            self.root = new_node
            return
        # if the tree is not empty
        self.insert_recursive_helper(self.root, new_node)

    # # Pre-Order (NLR) (Interative)
    # def pre_order_interative(self):
    #     if self.root == None:
    #         print("Tree is empty")
    #         return
        
    #     stack = []
    #     stack.append(self.root)
    #     while stack:
    #         current_node = stack.pop()
    #         print(current_node.value)
    #         if current_node.right:
    #             stack.append(current_node.right)
    #         if current_node.left:
    #             stack.append(current_node.left)
    
    # Pre-Order (NLR) (Recursive)
    def pre_order_recursive_helper(self, current_node):
        if current_node == None:
            return
        
        print(current_node.value)
        self.pre_order_recursive_helper(current_node.left)
        self.pre_order_recursive_helper(current_node.right)
    
    def pre_order_recursive(self):
        if self.root == None:
            print("Tree is empty")
            return
        
        self.pre_order_recursive_helper(self.root)

    
    # # Post-Order (LRN) (Interative)
    # def post_order_interative(self):
    #     if self.root == None:
    #         print("Tree is empty")
    #         return
        
    #     stack = []
    #     stack.append(self.root)
    #     while stack:
    #         current_node = stack.pop()
    #         print(current_node.value)
    #         if current_node.left:
    #             stack.append(current_node.left)
    #         if current_node.right:
    #             stack.append(current_node.right)
    
    # Post-Order (LRN) (Recursive)
    def post_order_recursive_helper(self, current_node):
        if current_node == None:
            return
        
        self.post_order_recursive_helper(current_node.left)
        self.post_order_recursive_helper(current_node.right)
        print(current_node.value)
    
    def post_order_recursive(self):
        if self.root == None:
            print("Tree is empty")
            return
        
        self.post_order_recursive_helper(self.root)

    # In-Order (LNR) (Interative)
    # def in_order_interative(self):
    #     if self.root == None:
    #         print("Tree is empty")
    #         return
        
    #     stack = []
    #     current_node = self.root
    #     while stack or current_node:
    #         while current_node:
    #             stack.append(current_node)
    #             current_node = current_node.left
    #         current_node = stack.pop()
    #         print(current_node.value)
    #         current_node = current_node.right
    
    # In-Order (LNR) (Recursive)
    def in_order_recursive_helper(self, current_node):
        if current_node == None:
            return
        
        self.in_order_recursive_helper(current_node.left)
        print(current_node.value)
        self.in_order_recursive_helper(current_node.right)

    def in_order_recursive(self):
        if self.root == None:
            print("Tree is empty")
            return
        
        self.in_order_recursive_helper(self.root)

    # Find Min (Interative)
    def find_min_interative(self):
        if self.root == None:
            print("Tree is empty")
            return
        
        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        print(current_node.value)

    # Find Min (Recursive)
    def find_min_recursive_helper(self, current_node):
        if current_node.left == None:
            print(current_node.value)
            return
        self.find_min_recursive_helper(current_node.left)

    def find_min_recursive(self):
        if self.root == None:
            print("Tree is empty")
            return
        
        self.find_min_recursive_helper(self.root)

    # Find Max (Interative)
    def find_max_interative(self):
        if self.root == None:
            print("Tree is empty")
            return
        
        current_node = self.root
        while current_node.right:
            current_node = current_node.right
        print(current_node.value)
    
    # Find Max (Recursive)
    def find_max_recursive_helper(self, current_node):
        if current_node.right == None:
            print(current_node.value)
            return
        self.find_max_recursive_helper(current_node.right)
    
    def find_max_recursive(self):
        if self.root == None:
            print("Tree is empty")
            return
        
        self.find_max_recursive_helper(self.root)

    # Find a Node (Interative)
    def find_node_interative(self, value):
        if self.root == None:
            print("Tree is empty")
            return
        
        current_node = self.root
        while current_node:
            if current_node.value == value:
                print("Node found")
                return
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        print("Node not found")

    # Find a Node (Recursive)
    def find_node_recursive_helper(self, current_node, value):
        if current_node == None:
            print("Node not found")
            return
        if current_node.value == value:
            print("Node found")
            return
        if value < current_node.value:
            self.find_node_recursive_helper(current_node.left, value)
        else:
            self.find_node_recursive_helper(current_node.right, value)

    def find_node_recursive(self, value):
        if self.root == None:
            print("Tree is empty")
            return
        
        self.find_node_recursive_helper(self.root, value)
    
    # Delete Node function
    # Delete Leaf Node
    # Delete Node with 1 Child
    # Delete Node with 2 Children
    # Delete Node (Interative)
    def delete_node_interative_findmax(self, value):
        if self.root == None:
            print("Tree is empty")
            return
        
        # Find the node to be deleted
        current_node = self.root
        parent_node = None
        while current_node and current_node.value != value:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            else:
                parent_node = current_node
                current_node = current_node.right
        
        if current_node == None:
            print("Node not found")
            return

        # if Delete Leaf Node
        if current_node.left == None and current_node.right == None :
            parent_node.left = None
        
        # if Delete Node with 1 Child
        elif current_node.left == None or current_node.right == None:
            if current_node.left == None:
                current_node = current_node.right
            else:
                current_node = current_node.left
        
        # if Delete Node with 2 Children
        else:
            # find the min node in the right subtree
            min_node = current_node.right
            while min_node.left == None:
                min_node = min_node.left
            current_node.value = min_node.value

            # delete the min node
            parent_node = current_node
            current_node = current_node.right
            while current_node.left:
                parent_node = current_node
                current_node = current_node.left
            parent_node.left = None

    # Delete Node function
    # Delete Leaf Node
    # Delete Node with 1 Child
    # Delete Node with 2 Children (left base is find max)
    def delete_node_interativ_findmax(self, value):
        if self.root == None:
            print("Tree is empty")
            return
        
        # Find the node to be deleted
        current_node = self.root
        parent_node = None
        while current_node and current_node.value != value:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            else:
                parent_node = current_node
                current_node = current_node.right
        
        if current_node == None:
            print("Node not found")
            return

        # if Delete Leaf Node
        if current_node.left == None and current_node.right == None :
            parent_node.left = None
        
        # if Delete Node with 1 Child
        elif current_node.left == None or current_node.right == None:
            if current_node.left == None:
                current_node = current_node.right
            else:
                current_node = current_node.left
        
        # if Delete Node with 2 Children (left base is find max)
        else:
            # find the max node in the left subtree
            max_node = current_node.left
            while max_node.right == None:
                max_node = max_node.right
            current_node.value = max_node.value

            # delete the max node
            parent_node = current_node
            current_node = current_node.left
            while current_node.right:
                parent_node = current_node
                current_node = current_node.right
            parent_node.right = None
