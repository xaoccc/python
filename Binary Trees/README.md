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
                self.left.create(self, data)

        # repeat the same check for the right branch
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.create(self, data)
   ```
   6. Insert data into the binary tree
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

   
       
