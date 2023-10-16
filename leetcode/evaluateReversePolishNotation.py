class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        myStack = []
      
        for x in tokens:
            if x == '+':
                myStack.append(myStack.pop() + myStack.pop())
            elif x == '-':
                a, b = myStack.pop(), myStack.pop()
                myStack.append(b-a)
            elif x == '*':
                myStack.append(myStack.pop() * myStack.pop())
            elif x == '/':
                a, b = myStack.pop(), myStack.pop()
                myStack.append(int(b/a))
            else:
                myStack.append(int(x))

        return myStack[0]