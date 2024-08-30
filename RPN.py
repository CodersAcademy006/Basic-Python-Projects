# Representing the node for the stack.
# The node class defines a constructor and the required getter and setter methods.

class Node:

   def __init__(self,d):
       self.data = d

   def setnext(self,n):
       self.next = n

   def getdata(self):
       return self.data

   def getnext(self):
       return self.next
# Representing the stack class.
# The stack class defines a constructor and the implementations for the
# push and pop operations. It also contains a method to check if the stack is empty.

class Stack:

   def __init__(self):
       self.top = None

   def push(self,d):
       self.newnode = Node(d)
       self.newnode.setnext(self.top)
       self.top = self.newnode

   def pop(self):
       temp = self.top
       self.top = self.top.getnext()
       n = temp.getdata()
       del temp
       return n

   def isempty(self):
       return self.top == None

import re

if __name__ == "__main__":
    try:
        mystack = Stack()
        expr = input("Enter expression with space between numbers and operators: ")
        expr = re.sub(" +"," ",expr)
        expr = expr.strip()
        elements = re.split(r"[\s]",expr)
        for x in elements:
            if x == "+":
                n1 = int(mystack.pop())
                n2 = int(mystack.pop())
                n3 = n2 + n1
                mystack.push(n3)
            elif x == "-":
                n1 = int(mystack.pop())
                n2 = int(mystack.pop())
                n3 = n2 - n1
                mystack.push(n3)
            elif x == "*":
                n1 = int(mystack.pop())
                n2 = int(mystack.pop())
                n3 = n2 * n1
                mystack.push(n3)
            elif x == "//":
                n1 = int(mystack.pop())
                n2 = int(mystack.pop())
                n3 = n2 // n1
                mystack.push(n3)
            elif x == "/":
                n1 = int(mystack.pop())
                n2 = int(mystack.pop())
                n3 = n2 / n1
                mystack.push(n3)
            else:
                mystack.push(x)
        print("Result: " + str(mystack.pop()))
    except AttributeError as e:
        print("Invalid Expression: " + str(e))
