#!/usr/bin/env/python3


class ListNode:
    value = None
    next = None

    def __init__(self, val=None, nxt=None):
        self.value = val
        self.next = nxt


class PointerList:
    head = None
    num_nodes = 0

    def __init__(self):
        self.head = ListNode()  # Initialize a List to have an empty node in it
        self.num_nodes = 0

    def FIRST(self):
        if self.head.value is not None:
            return 0
        else:
            return -1

    def END(self):
        if self.num_nodes > 0:
            return self.num_nodes + 1
        else:
            return -1

    def RETRIEVE(self, p):
        # Nice try guy
        if p < 0:
            return -1
        # Check to see if p is a possible position in the list
        if p > self.num_nodes:
            return -1

        # Loop through the List and keep track of how many nodes have been looked at
        counter = 0
        current = self.head
        while current.next is not None:
            if counter == p:
                break
            else:
                current = current.next
                counter = counter + 1

        # Return the value of the node at p
        return current.value

    def LOCATE(self, x):
        counter = 0
        current = self.head
        while current is not None:
            if current.value == x:
                return counter
            else:
                current = current.next
                counter = counter + 1

    def NEXT(self, p):
        counter = 0
        current = self.head
        while current is not None:
            if counter == p:
                return counter + 1
            else:
                current = current.next
                counter = counter + 1

    def PREVIOUS(self, p):
        counter = 0
        current = self.head
        while current is not None:
            if counter == p:
                return counter - 1
            else:
                current = current.next
                counter = counter + 1

    def INSERT(self, p, x):
        if self.head.value is None:
            # If there's nothing in the list, then position doesn't even matter
            # Make the head equal to x
            self.head.value = x
            self.num_nodes = self.num_nodes + 1
            return
        elif p < 0:
            return  # Nice try guy
        elif p >= self.num_nodes:
            # If position is greater than number of nodes, then it goes at the end
            # Get the node that is at the end
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            # Set it's next equal to a new node with value x
            current_node.next = ListNode(x)
            self.num_nodes = self.num_nodes + 1
        elif p < self.num_nodes:
            # This is where things get crazy...
            # Gotta insert a node where p is and shift all nodes over...
            current_node = self.head
            counter = 0
            while current_node.next is not None:
                if counter == p - 1:
                    break
                else:
                    current_node = current_node.next
                    counter = counter + 1

            # Current_node is now the node right before position p // p_node is node at p
            p_node = current_node.next

            # Our new node's next should be p_node and our current node's next is our new node
            new_node = ListNode(x, p_node)
            current_node.next = new_node

    def DELETE(self, p):
        counter = 0
        current = self.head
        while current is not None:
            if counter == (p - 1):
                # Current will be the node before p
                # After is the node after p
                after = current.next.next
                # Set current's next equal to after (therefore deleting p)
                current.next = after
            else:
                current = current.next
                counter = counter + 1

    def MAKENULL(self):
        # Make the head be an empty node to make entire list mull
        self.head = ListNode()

    def display(self):
        current = self.head
        while current is not None:
            print("{0} ".format(current.value))
            current = current.next
