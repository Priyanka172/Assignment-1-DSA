def sortStack ( stack ):
    tmpStack = createStack()
    while(isEmpty(stack) == False):
         
        # pop out the first element
        tmp = top(stack)
        pop(stack)
 
        # while temporary stack is not
        # empty and top of stack is
        # greater than temp
        while(isEmpty(tmpStack) == False and
             int(top(tmpStack)) > int(tmp)):
             
            # pop from temporary stack and
            # push it to the input stack
            push(stack,top(tmpStack))
            pop(tmpStack)
 
        # push temp in temporary of stack
        push(tmpStack,tmp)
     
    return tmpStack
 
# Function to create a stack.
# It initializes size of stack
# as 0
def createStack():
    stack = []
    return stack
 
# Function to check if
# the stack is empty
def isEmpty( stack ):
    return len(stack) == 0
 
# Function to push an
# item to stack
def push( stack, item ):
    stack.append( item )
 
# Function to get top
# item of stack
def top( stack ):
    p = len(stack)
    return stack[p-1]
 
# Function to pop an
# item from stack
def pop( stack ):
 
    # If stack is empty
    # then error
    if(isEmpty( stack )):
        print("Stack Underflow ")
        exit(1)
 
    return stack.pop()
 
# Function to print the stack
def prints(stack):
    for i in range(len(stack)):
        print(stack[0])
        break
    
 
# Driver Code
stack = createStack()
push( stack, 34 )
push( stack, 3 )
push( stack, 31 )
push( stack, 98 )
push( stack, 92 )
push( stack, 23 )
 
print("The smallest number is ")
sortedst = sortStack ( stack )
prints(sortedst)