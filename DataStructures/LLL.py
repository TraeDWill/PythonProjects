#Here is where I work on LLL's

#Node that has 2 members, data and next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Linear Linked List class
#Data Members: Head
class LLL:
    def __init__(self):
        self.head = None


    def insertAtHead(self, data):
        """
        Inserts a new node at the head of the LLL

        Arguments: 
            self(LLL): The LLL that is being manipulated
            data(int): The data which is being added into the LLL

        return:
            None
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
            return
    
    def insertAtTail(self, data):
        """
        Inserts a new node at the tail of the LLL

        Arguments: 
            self(LLL): The LLL that is being manipulated
            data(int): The data which is being added into the LLL

        return:
            None
        """
        new_node = Node(data)
        finder = self.head
        while finder.next is not None:
            finder = finder.next
        finder.next = new_node
        return

    def insertAfterValue(self, data, search):
        """
        Inserts a new node at the tail of the LLL

        Arguments: 
            self(LLL): The LLL that is being manipulated
            data(int): The data which is being added into the LLL

        return:
            None
        """
        new_node = Node(data)
        finder = self.head
        next_node = None
        while finder.data is not search:
            finder = finder.next
            if finder.head is None:
                print("Unable to find such value.")
                return
        next_node = finder.next
        finder.next = new_node
        new_node.next = next_node
        return
    

    def removeHead(self):
        """
        This function removes the head node from the LLL

        Arguments: 
            self(LLL): The LLL that is being manipulated

        Return
            int: The data which is being removed from the LLL
        """
        removed = None
        if self.head is None:
            print("The LLL is empty.")
            return
        else:
            removed = self.head
            self.head = self.head.next
            return removed.data
        
    def removeTail(self):
        """
        This function removes the tail node from the LLL

        Arguments: 
            self(LLL): The LLL that is being manipulated

        Return
            int: The data which is being removed from the LLL
        """
        finder = self.head
        drag = None
        if self.head is None:
            print("The LLL is empty.")
            return
        else:
            while finder.next is not None:
                drag = finder
                finder = finder.next
            drag.next = None
            return finder.data
        
    def removeNodeOfValue(self, remove):
        """
        This function removes every node of a certain value

        Args:
            self(LLL): The list which the value is being removed from

            remove(int): The value that is being removed from the list

            count(int): The number of nodes removed

        return
            The number of nodes that are removed
        """
        finder = self.head
        drag = finder
        count = 0
        if self.head is None:
            print("The LLL is empty.")
            return
        while finder is not None:
            if finder is self.head and finder.data is remove:
                self.removeHead(self)
                finder = self.head
                count += 1
            elif finder.next is None and finder.data is remove:
                self.removeTail(self)
                count += 1
                return count
            elif finder.data is remove:
                drag.next = finder.next
                finder = drag.next
                count += 1
            else:
                drag = finder
                finder = finder.next

    def displayAll(self):
        """
        This function displays all of the values in a linear linked list

        Args:
            self(LLL): The linear linked list which is being display

        Return:
            None
        """
        display = self.head
        total = 0
        if self.head is None:
            print("The list is empty.")
        while display is not None:
            print(f'{display.data} | ')
            total += display.data
        print(f'Total is: {total}')
        return
            

    
