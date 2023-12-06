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
       
