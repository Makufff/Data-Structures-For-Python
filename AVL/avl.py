# avl_tree_with_linkedlist.py

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            print(f"LinkedList: Appended first element {value}.")
        else:
            self.tail.next = new_node
            self.tail = new_node
            print(f"LinkedList: Appended element {value}.")

class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, value):
        if not root:
            print(f"AVLTree: Inserting value {value} as a new node.")
            return AVLNode(value)
        elif value < root.value:
            print(f"AVLTree: Inserting value {value} to the left of {root.value}.")
            root.left = self.insert(root.left, value)
        elif value > root.value:
            print(f"AVLTree: Inserting value {value} to the right of {root.value}.")
            root.right = self.insert(root.right, value)
        else:
            print(f"AVLTree: Duplicate value {value} not inserted.")
            return root

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        print(f"AVLTree: Updated height of node {root.value} to {root.height}.")

        balance = self.get_balance(root)
        print(f"AVLTree: Balance factor of node {root.value} is {balance}.")

        # Case 1 - Left Left
        if balance > 1 and value < root.left.value:
            print(f"AVLTree: Left Left Case detected at node {root.value}. Performing right rotation.")
            return self.right_rotate(root)

        # Case 2 - Right Right
        if balance < -1 and value > root.right.value:
            print(f"AVLTree: Right Right Case detected at node {root.value}. Performing left rotation.")
            return self.left_rotate(root)

        # Case 3 - Left Right
        if balance > 1 and value > root.left.value:
            print(f"AVLTree: Left Right Case detected at node {root.value}. Performing left rotation on left child then right rotation.")
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 4 - Right Left
        if balance < -1 and value < root.right.value:
            print(f"AVLTree: Right Left Case detected at node {root.value}. Performing right rotation on right child then left rotation.")
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, value):
        if not root:
            print(f"AVLTree: value {value} not found for deletion.")
            return root

        if value < root.value:
            print(f"AVLTree: Deleting value {value} from the left of {root.value}.")
            root.left = self.delete(root.left, value)
        elif value > root.value:
            print(f"AVLTree: Deleting value {value} from the right of {root.value}.")
            root.right = self.delete(root.right, value)
        else:
            print(f"AVLTree: Deleting value {value} found at node {root.value}.")
            if not root.left:
                temp = root.right
                print(f"AVLTree: Node {root.value} has no left child. Replacing with right child.")
                root = None
                return temp
            elif not root.right:
                temp = root.left
                print(f"AVLTree: Node {root.value} has no right child. Replacing with left child.")
                root = None
                return temp

            temp = self.get_min_value_node(root.right)
            print(f"AVLTree: Node {root.value} has two children. Inorder successor is {temp.value}. Replacing value.")
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if not root:
            return root

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        print(f"AVLTree: Updated height of node {root.value} to {root.height} after deletion.")

        balance = self.get_balance(root)
        print(f"AVLTree: Balance factor of node {root.value} is {balance} after deletion.")

        # Case 1 - Left Left
        if balance > 1 and self.get_balance(root.left) >= 0:
            print(f"AVLTree: Left Left Case detected at node {root.value} after deletion. Performing right rotation.")
            return self.right_rotate(root)

        # Case 2 - Left Right
        if balance > 1 and self.get_balance(root.left) < 0:
            print(f"AVLTree: Left Right Case detected at node {root.value} after deletion. Performing left rotation on left child then right rotation.")
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 3 - Right Right
        if balance < -1 and self.get_balance(root.right) <= 0:
            print(f"AVLTree: Right Right Case detected at node {root.value} after deletion. Performing left rotation.")
            return self.left_rotate(root)

        # Case 4 - Right Left
        if balance < -1 and self.get_balance(root.right) > 0:
            print(f"AVLTree: Right Left Case detected at node {root.value} after deletion. Performing right rotation on right child then left rotation.")
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        print(f"AVLTree: Performing left rotation on node {z.value}.")

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        print(f"AVLTree: Updated heights after left rotation: {z.value} -> {z.height}, {y.value} -> {y.height}.")

        return y

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        print(f"AVLTree: Performing right rotation on node {y.value}.")

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left),
                           self.get_height(x.right))
        print(f"AVLTree: Updated heights after right rotation: {y.value} -> {y.height}, {x.value} -> {x.height}.")

        return x

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def pre_order(self, root):
        linked_list = LinkedList()
        self._pre_order_helper(root, linked_list)
        return linked_list

    def _pre_order_helper(self, node, linked_list):
        if node:
            linked_list.append(node.value)
            self._pre_order_helper(node.left, linked_list)
            self._pre_order_helper(node.right, linked_list)

    def in_order(self, root):
        linked_list = LinkedList()
        self._in_order_helper(root, linked_list)
        return linked_list

    def _in_order_helper(self, node, linked_list):
        if node:
            self._in_order_helper(node.left, linked_list)
            linked_list.append(node.value)
            self._in_order_helper(node.right, linked_list)

    def post_order(self, root):
        linked_list = LinkedList()
        self._post_order_helper(root, linked_list)
        return linked_list

    def _post_order_helper(self, node, linked_list):
        if node:
            self._post_order_helper(node.left, linked_list)
            self._post_order_helper(node.right, linked_list)
            linked_list.append(node.value)

    def search(self, root, value):
        if not root:
            print(f"AVLTree: value {value} not found in the tree.")
            return False
        if value == root.value:
            print(f"AVLTree: value {value} found.")
            return True
        elif value < root.value:
            return self.search(root.left, value)
        else:
            return self.search(root.right, value)

    def is_balanced(self, root):
        if not root:
            return True

        balance = self.get_balance(root)
        if balance > 1 or balance < -1:
            return False

        return self.is_balanced(root.left) and self.is_balanced(root.right)

def main():
    tree = AVLTree()
    root = None

    values_to_insert = [10, 20, 30, 40, 50, 25]
    print("\n--- Inserting Nodes ---")
    for value in values_to_insert:
        root = tree.insert(root, value)
        pre_order_ll = tree.pre_order(root)
        print(f"Inserted {value}, Pre-order traversal: {pre_order_ll}")

    in_order_ll = tree.in_order(root)
    print(f"\nIn-order traversal after insertions: {in_order_ll}")

    post_order_ll = tree.post_order(root)
    print(f"Post-order traversal after insertions: {post_order_ll}")

    search_value = 25
    print(f"\n--- Searching for value {search_value} ---")
    found = tree.search(root, search_value)
    print(f"Search for {search_value}: {'Found' if found else 'Not Found'}")

    value_to_delete = 40
    print(f"\n--- Deleting value {value_to_delete} ---")
    root = tree.delete(root, value_to_delete)
    pre_order_ll = tree.pre_order(root)
    print(f"Deleted {value_to_delete}, Pre-order traversal: {pre_order_ll}")

    in_order_ll = tree.in_order(root)
    print(f"In-order traversal after deletion: {in_order_ll}")

    post_order_ll = tree.post_order(root)
    print(f"Post-order traversal after deletion: {post_order_ll}")

    print(f"\n--- Checking if the tree is balanced ---")
    balanced = tree.is_balanced(root)
    print(f"Tree is {'balanced' if balanced else 'not balanced'}.")

if __name__ == "__main__":
    main()
