class BoundedStack:
    peek_nil = 0
    pop_nil = 0
    peek_ok = 1
    pop_ok = 1
    peek_err = 2
    pop_err = 2

    def __init__(self, size=32):
        self.size = size
        self.stack = [] * self.size
        self.peek_status = 0
        self.pop_status = 0

    def push(self, value):
        self.stack.append(value)

    def size(self):
        return len(self.stack)




