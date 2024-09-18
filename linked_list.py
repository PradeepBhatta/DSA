class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node


    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)


    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0 :
            self.insert_at_beginning(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1 :
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1 
    
    def insert_after_value(self, data_after, data_to_insert):
        if self.head == None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next


    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0 :
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1 :
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
             

    def remove(self, data):
        if self.head == None:
            return

        if self.head.data == data:
            self.head = self.head.next

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break    
            itr = itr.next


    def add_values(self, lst):
        for data in lst:
            self.insert_at_end(data)


    def print(self):
        itr = self.head
        llstr = ''
        while itr:
            suffix = ''
            if itr.next :
                suffix = ' --> '
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr)

    def is_empty(self):
        return self.head == None

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

if  __name__ == '__main__':
    root = LinkedList()
    print("Is Linked List empty? ",root.is_empty())
    root.insert_at_end(20)
    root.insert_at_beginning(15)
    root.insert_at_beginning(10)
    root.insert_at_beginning(5)
    root.insert_at_end(30)
    root.insert_at(4, 25)
    root.insert_at(4, 25)
    root.print()
    root.remove_at(4)
    root.print()
    print("No. of Elements = ",root.get_length())
    print("Is Linked List empty? ",root.is_empty())
    lst = ["apple", "ball", "cat"]
    root.add_values(lst)
    root.remove(25)
    root.print()
    root.insert_after_value(20, 25)
    root.print()


    