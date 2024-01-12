class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(node, value):
    if node is None:
        return Node(value)
    
    if value < node.value:
        node.left = insert(node.left, value)
    elif value > node.value:
        node.right = insert(node.right, value)
    
    return node

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    
    return current

def delete(node, value):
    if node is None:
        return node
    
    if value < node.value:
        node.left = delete(node.left, value)
    elif value > node.value:
        node.right = delete(node.right, value)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp
        else: 
            successor = min_value_node(node.right)
            node.value = successor.value
            node.right = delete(node.right, value)
    return node

def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.value, end = ' ')
    inorder_traversal(node.right)

def preorder_traversal(node):
    if node is None:
        return
    print(node.value, end = ' ')
    preorder_traversal(node.left)
    preorder_traversal(node.right)

def postorder_traversal(node):
    if node is None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.value, end = ' ')

def main():
    root = Node(50)
    
    # insert some nodes
    insert(root, 100)
    insert(root, 10)
    insert(root, 15)
    insert(root, 60)
    insert(root, 55)
    
    # show various traversal orders
    inorder_traversal(root)
    print('\n')
    preorder_traversal(root)
    print('\n')
    postorder_traversal(root)
    print('\n')

    # remove some nodes
    delete(root, 100)
    delete(root, 150)

    # show new order
    inorder_traversal(root)
    print('\n')

if __name__ == "__main__":
    main()