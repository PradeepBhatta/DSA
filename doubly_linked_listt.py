class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
            

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)


    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0 :
            self.insert_at_beginning(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1 :
                node = Node(data, itr.next, itr)
                if node.next :
                    node.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1 
    
    def insert_after_value(self, data_after, data_to_insert):
        if self.head == None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next, None)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                itr.next = node

                if node.next :
                    node.next.prev = node            

                break
            itr = itr.next


    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0 :
            self.head = self.head.next
            self.head.prev = None
            return

        itr = self.head
        count = 0
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next
            count += 1
             

    def remove(self, data):
        if self.head == None:
            return

        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                if itr.next:
                    itr.next.prev = itr.next
                break    
            itr = itr.next


    def add_values(self, lst):
        for data in lst:
            self.insert_at_end(data)


    def is_empty(self):
        return self.head == None

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr


    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            suffix = ''
            if itr.next :
                suffix = ' --> '
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            suffix = ''
            if itr.prev:
                suffix = ' --> '
            llstr += str(itr.data) + suffix
            itr = itr.prev
        print("Link list in reverse: ", llstr)


if  __name__ == '__main__':
    ll = DoublyLinkedList()
    print("Is Linked List empty? ",ll.is_empty())
    ll.insert_at_end(20)
    ll.insert_at_beginning(15)
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(5)
    ll.insert_at_end(30)
    ll.insert_at(4, 25)
    ll.insert_at(4, 25)
    ll.print_forward()
    ll.remove_at(4)
    ll.print_forward()
    print("No. of Elements = ",ll.get_length())
    print("Is Linked List empty? ",ll.is_empty())
    lst = ['apple', 'ball', 'cat']
    ll.add_values(lst)
    ll.remove(25)
    ll.print_forward()
    ll.insert_after_value(20, 25)
    ll.print_forward()
    ll.print_backward()


    