Notes about binary trees:
1. Each node  in a binary tree can have up to 2 children, otherwise is becomes a graph
2. Left child is always smaller than right child\
3. A Node is a tree
4. Define a tree  
    ```
    class Node:
    def __init__(self, data):   
        self.left = None   
        self.right = None   
        self.data = data
    ```
5. Create a node. We use the word 'create', not 'insert', because of CRUD
   ```
    def create(self, data):
        # if head has no data, we insert current data
        if self.data is None:
            self.data = data

        # then check left branch
        elif data < self.data:
            # if empty, populate it with data
            if self.left is None:
                self.left = Node(data)
            # if the branch has data, it becomes the head of a new branch, and we create the new branch.
            # recursively we search for an empty branch on the left until we find one
            else:
                self.left.create(data)

        # repeat the same check for the right branch
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.create(data)
   ```
   
6. Insert Data Into the Binary Tree
   
   Important!!!
    - You cannot create a binary tree with different data types. If you try to do this, you will receive a TypeError.
    - Here we cannot create a branch with the same value as the head. Thus nodes are unique. However, you can create equal tree nodes, just by replacing '>' with '>='. 
   ```
   root = Node(5)
   print(root.data)
   print(root.left)
   print(root.right)
   root.create(7)
   print(root.data)
   print(root.left)
   print(root.right.data)
   root.create(3)
   print(root.data)
   print(root.left.data)
   print(root.right.data)
    ```
   
   You can see, that we have a small binary tree, which looks like this:  
   ![image](https://github.com/xaoccc/python/assets/114498517/1a3561eb-5499-41e5-8958-b87ed34a730e)
   
7.  InOrder Traversal of a Binary Tree
We do this recursively in direction left -> head -> right, starting from the leftmost, lowest tree node. In our example, it will be: 3, 5, 7
If we add node with data=17, the result will be: 3, 5, 7, 17
```
def InOrderPrint(root):
    if root.left is not None:
        InOrderPrint(root.left)
    print(root.data)
    if root.right is not None:
        InOrderPrint(root.right)


InOrderPrint(root)
```
8. PreOrder Traversal of a Binary Tree
We do this recursively in direction head -> left -> right
You see that we simply excahnged the places of head and left in the function
```
def PreOrderPrint(root):
    print(root.data)
    if root.left is not None:
        PreOrderPrint(root.left)    
    if root.right is not None:
        PreOrderPrint(root.right)


PreOrderPrint(root)
```
9. PostOrder Traversal of a Binary Tree
We do this recursively in direction left -> right -> head
As you see, we can change the order in which we traverse a binary tree. There are 2 more possible traversals, but they are not very popular:
- right -> head -> left
- right -> left -> head
```
def PostOrderPrint(root):    
    if root.left is not None:
        PostOrderPrint(root.left)    
    if root.right is not None:
        PostOrderPrint(root.right)
    print(root.data)


PostOrderPrint(root)
```
10. Breadth First Search (using root as an argument)
10.1. create dictionary to store all data in format {node: [child1, child2, ...], ...}
10.2. define the only base condition: check if there is a node, if not return
10.3. traverse through the left and the right in width and depth, recursively and fill the data into the dictionary
10.4. at this point we have all data from our binary tree and using a queue and another dictionary, we reformat the data into the new dictionary
11. Depth First Search (using root as an argument)
Here we do as in BFS, except here we use a stack instead of queue and check for visited nodes.

 
   
       
