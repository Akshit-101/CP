# ---------------- Implement Stack using single Queue --------------
from queue import Queue

class Stack:
    def __init__(self):
        self.q = Queue()


    def push(self, x):
        s = self.q.qsize()
        self.q.put(x)
        for i in range(s):
            self.q.put(self.q.get())


    def pop(self):
        n = self.q.get()
        return n


    def top(self):
        return self.q.queue[0]


    def size(self):
        return self.q.qsize()




if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.push(2)
    s.push(4)
    s.push(1)
    print("Top of the stack: ", s.top())
    print("Size of the stack before removing element: ", s.size())
    print("The deleted element is: ", s.pop())
    print("Top of the stack after removing element: ", s.top())
    print("Size of the stack after removing element: ", s.size())


    # ------------------- Implement Queue using Stack --------------------

    from queue import LifoQueue
# using LifoQueue which is a stack in python




class Queue:
    def __init__(self):
        self.input = LifoQueue()
        self.output = LifoQueue()


    def push(self, data: int) -> None:
        # Pop out all elements from the stack input
        while not self.input.empty():
            self.output.put(self.input.get())
        # Insert the desired element in the stack input
        print("The element pushed is", data)
        self.input.put(data)
        # Pop out elements from the stack output and push them into the stack input
        while not self.output.empty():
            self.input.put(self.output.get())


    # Pop the element from the Queue
    def pop(self) -> int:
        if self.input.qsize() == 0:
            print("Stack is empty")
            exit(0)
        val = self.input.get()
        return val


    def Top(self) -> int:
        if self.input.qsize() == 0:
            print("Stack is empty")
            exit(0)
        return self.input.queue[-1]


    def size(self) -> int:
        return self.input.qsize()




if __name__ == "__main__":
    q = Queue()
    q.push(3)
    q.push(4)
    print("The element poped is", q.pop())
    q.push(5)
    print("The top of the queue is", q.Top())
    print("The size of the queue is", q.size())
