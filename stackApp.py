# Pop operation
class PopStack:
    def __init__(self, max_size):
        self.stack = []
        self.top = -1
        self.max_size = max_size

    def is_full(self):
        return self.top == self.max_size - 1
    
    def is_empty(self):
        return self.top == -1
    
    def push(self, data):
        if not self.is_full():
            if data not in self.stack:
                self.top += 1
                self.stack.append(data)
                #check if it is successfully pushed
                return True
            else:
                #element is already in stack
                return False
        else:
            #stack is full or overflow
            return "Stack overflow"
        
    def pop(self):
        if not self.is_empty():
            popped_element  = self.stack[self.top]
            self.top -= 1
            return popped_element
        else:
            return "Stack underflow"
        
    def display_elements(self):
        if self.is_empty():
            print("Stack underflow")
        else:
            print("Elements in stack list: ")
            for i in range(self.top + 1):
                print(self.stack[i])

#create a stack with a maximum of five
stack = PopStack(5)

#push elements
print(stack.push("Kristian"))
print(stack.push("Gerald"))
print(stack.push("Cura"))
print(stack.push("Gabot"))
print(stack.push("Xian"))
print(stack.push("Dara"))

stack.display_elements()

#removing the element one by one from stack
print("Popping elements one by one: ")

while not stack.is_empty():
    popped = stack.pop()
    print("Removed Element: ",  popped)
stack.display_elements()