"""Implementation of Stack using LinkedList
    Main Principle of Stack is LIFO(Last in First Out)
    """
#Program Witten By Manendra Nath Shukla
#now Lets Declare Node class
class Node:
    def __init__(self,data):  #Constructor to instialize the new Node for the given data
        self.data=data
        self.next=None

class Stack:            # Stack Class Like LinkedList
    def __init__(self):
        self.top=None          #by default we don't have any Node in Stack So top will be None


    def push(self,data):        #method to insert element in Stack 
        new=Node(data)          #new node to insert 
        if(self.top is None):       
            #print("pushed")
            self.top=new
            return 
        #print("pused in stck")
        temp=self.top
        new.next=temp
        self.top=new


    def pop(self):          #method to remove a last inserted element 
        if(self.top is None):
            print("Stack Underflow") #if stack is empty
            return
        #print("Poped")
        self.top=self.top.next

    def display(self):  #display the stack data
        temp=self.top
        while(temp is not None):
            print(temp.data)
            temp=temp.next
        

if __name__ == "__main__":
    tru=True

    myStack=Stack()
   
    ch=True
    while(tru):
        print("*"*50)
        print("                   Stack Dashboard          ")
        print("*"*50)
        print("1.Push")
        print("2.Pop")
        print("3.Display Stack Elements")
        print("4.Exit")
        ch=int(input("Enter Your Choice:"))
        if(ch==1):
            d=input("Enter Element to be Pushed in Stack:")
            myStack.push(d)
            print("Data is Pushed in Stack Successfully")
        if(ch==2):
            myStack.pop()
            print("Stack Element is Popped  Sucessfully")
        if(ch==3):
            print("Stack Elements are:")
            myStack.display()
        if(ch==4):
            tru=False
            
            