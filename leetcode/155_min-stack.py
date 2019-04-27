# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
#     push(x) -- Push element x onto stack.
#     pop() -- Removes the element on top of the stack.
#     top() -- Get the top element.
#     getMin() -- Retrieve the minimum element in the stack.
# Example:
#     MinStack minStack = new MinStack();
#     minStack.push(-2);
#     minStack.push(0);
#     minStack.push(-3);
#     minStack.getMin();   --> Returns -3.
#     minStack.pop();
#     minStack.top();      --> Returns 0.
#     minStack.getMin();   --> Returns -2.

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            self.min = min(self.min, x)


    def pop(self):
        """
        :rtype: void
        """
        if self.stack[-1] < 0:
            self.min -= self.stack[-1]
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.min if self.stack[-1] < 0 else self.min + self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()