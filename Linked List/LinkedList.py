class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    def pop(self):
        pre = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            pre = None            
            self.tail = None
            self.length = 0
            return pre
        else:
            temp = self.head
            while(temp.next):
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1  
            return temp
    def pop_first(self):
        temp = self.head
        if self.length == 0:
            return None
        else:
            self.head = self.head.next 
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp   
    def get(self,index):
        if index <0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
    def set_value(self, index, value):
        if index <0 or index >= self.length:
            return False
        else:
            temp = self.get(index)
            temp.value = value 
            return self  
    def insert_value(self, index, value):
        if index <0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return self
    def remove(self, index):
        if index <0 or index >= self.length:
            raise IndexError("Index out of bounds")
        if index == self.length -1:
            self.pop()
        elif index == 0:
            self.pop_first()
        else: 
            pre = self.get(index-1)
            temp = pre.next
            pre.next = temp.next
            temp.next = None
            self.length -= 1
        return self
    def reverse(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            return self
        else: 
            temp = self.head
            self.head = self.tail
            self.tail = temp
            before = None
            for _ in range (self.length):
                after = temp.next
                temp.next = before
                before = temp
                temp = after
            return self
my_linked_list = LinkedList(2)
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)
my_linked_list.append(3)
my_linked_list.prepend(7)
print('Linked List:')
my_linked_list.print_list()
my_linked_list.reverse()
popped_node = my_linked_list.pop()
print(popped_node.value)
print(my_linked_list.pop_first().value)
print(my_linked_list.get(0).value)
new_list = my_linked_list.set_value(0,13)
new_list.print_list()
new_insert_list = my_linked_list.insert_value(1,17)
new_insert_list.print_list()
my_linked_list.remove(0).print_list()
