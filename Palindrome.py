class Stack:
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
            self.top += 1
            self.stack.append(data)
            #check if it is successfully pushed
            return data

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


word = input("Enter a word: ") #kayak
word_updated = word.replace(" ", "")


length = len(word_updated) #5

stack = Stack(length)

pushed = []
i = 0

print("Pushed Elements: ")
while i < length: #0 < 5
    pushed += word_updated[i]
    print(stack.push(pushed[i]))
    i+=1

popped = []
j = 0

print("Popped Elements: ")
while not stack.is_empty() and j < length:
    popped += stack.pop()
    print(popped[j])
    j += 1

# print(popped)
if popped == pushed:
    print(f"\nThe word {word} is a palindrome.")
else:
    print(f"\nThe word {word} is not a palindrome.")