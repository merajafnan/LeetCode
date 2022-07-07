# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
# Implement the MyStack class:
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise
#
# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

class MyStack:

    def __init__(self):
        self.q = deque()


    def push(self, x: int) -> None:
        return(self.q.append(x))


    def pop(self) -> int:
        for i in range(len(self.q)-1):
            z = self.q.popleft()
            self.q.append(z)
        return self.q.popleft()


    def top(self) -> int:
        return (self.q[-1])


    def empty(self) -> bool:
        if len(self.q) == 0:
            return True




# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()