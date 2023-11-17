#linked list is a linear data structure where each element is separate object called node
# a node contains two items: data and reference (next node)

class Node:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.next = None
        
class PushLink:
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        return self.top is None
    
    def push(self, name, grade):
        new_node = Node(name, grade)
        new_node.next = self.top
        self.top = new_node
        
    def pop(self):
        #Mini-activity create the pop for this node.
        if not self.is_empty():
            popped_node = self.top
            self.top = self.top.next
            return popped_node.name, popped_node.grade
        
        else:
            return "List is empty"
        
    def peek(self):
        if self.is_empty():
            return None
        return self.top.name, self.top.grade
        
s = PushLink()

# s.push("Xian", 99)
# s.push("Bets", 99)
# s.push("Aren", 99)

print(s.peek())
print(s.pop())
print(s.pop())
print(s.peek())