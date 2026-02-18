class MinStack:
    '''
    Solution for Min Stack

    Here, the objective is to write a class with different methods for different functionalities of the stack
    The catch here is all of them have to be O(1)
    since we're using lists as the stack data structure, all the regular operations like pop, push and top will be O(1)
    But getMin will be a little complex. 
    So what i do is i have another stack running parallely. 
    While pushing to the original stack, I also check whether the current element is smaller than the top element of the parallel stack
    If it is smaller, i push the minimum element to the parallel stack
    This way, the top of the parallel stack is always going to be the smallest element in the original stack
    '''

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, element):
        self.stack.append(element)
        if self.minstack:
            self.minstack.append(min(element, self.minstack[-1]))
        else:
            self.minstack.append(element)
        return None

    def pop(self):
        self.stack.pop()
        self.minstack.pop()
        return None
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minstack[-1]

if __name__ == "__main__":

    commands = ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"] 
    output = []
    for i, command in enumerate(commands):
        if command == 'MinStack':
            ms = MinStack()
            output.append(None)
        elif command == 'push':
            output.append(ms.push(commands[i+1]))
        elif command == 'pop':
            output.append(ms.pop())
        elif command == 'top':
            output.append(ms.top())
        elif command == 'getMin':
            output.append(ms.getMin())
        else:
            continue

    print(output)