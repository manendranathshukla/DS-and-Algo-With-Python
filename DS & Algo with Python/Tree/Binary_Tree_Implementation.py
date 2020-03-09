
class Node:
    def __init__(self,da):
        self.data=da
        self.left=None 
        self.right=None


class BinaryTree:
    def __init__(self,value):
        self.root=Node(value)

    



    def print_tree(self,traversal_type):
        if(traversal_type=="preorder"):
            return self.pre_order(self.root,"")
        if(traversal_type=="inorder"):
            return self.in_order(self.root,"")
        if(traversal_type=="postorder"):
            return self.post_order(self.root,"")
        else:
            return "not a traversal type"

    def pre_order(self,start,traversal):
        if(start):
            traversal+=(str(start.data)+"->")
            traversal=self.pre_order(start.left,traversal)
            traversal=self.pre_order(start.right,traversal)
        
        return traversal
    def in_order(self,start,traversal):
        if(start):
            
            traversal=self.pre_order(start.left,traversal)
            traversal+=(str(start.data)+"->")
            traversal=self.pre_order(start.right,traversal)
        
        return traversal
    def post_order(self,start,traversal):
        if(start):
            
            traversal=self.pre_order(start.left,traversal)
            
            traversal=self.pre_order(start.right,traversal)
            traversal+=(str(start.data)+"->")
        
        return traversal



    def height_of_tree(self,node):
        if node is None:
            return -1 
        l=self.height_of_tree(node.left)
        r=self.height_of_tree(node.right)
        return max(l,r)+1


    def size(self):
        if self.root is None:
            return 0
        stack=Stack()

b=BinaryTree(10)
b.root.left=Node(5)
b.root.right=Node(7)
b.root.left.left=Node(12)
b.root.left.right=Node(4)
b.root.right.left=Node(3)
b.root.right.right=Node(1)
print("Pre Order " +b.print_tree("preorder"))
print("In Order " + b.print_tree("inorder"))
print("Post order "+b.print_tree("postorder"))
print("Height:"+str(b.height_of_tree(b.root)))
