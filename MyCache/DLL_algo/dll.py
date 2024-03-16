from .node import *
class DLinkedList:
        def __init__(self,freq):
            self.freq = freq
            self.head = Node(0, 0)
            self.tail = Node(0, 0)
            self.head.next = self.tail
            self.tail.prev = self.head

        def add_node_at_head(self, node):
            t = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next = t
            t.prev = node

        def add_node_at_last(self, node):
            p = self.tail.prev
            p.next = node
            self.tail.prev = node
            node.prev = p
            node.next = self.tail

        def add_element_at_last(self,key):
             node = Node(key,key)
             self.add_node_at_last(node)
             return node
        
        def add_element_at_head(self,key):
             node = Node(key,key)
             self.add_node_at_head(node)
             return node
 
 
        def is_empty(self):
            return self.head.next == self.tail

        def detach_node(self, node):
            node.next.prev = node.prev
            node.prev.next = node.next

        def pop(self):
            if self.is_empty():
                return None
            node = self.tail.prev
            self.detach_node(node)
            return node
        
        def get_first_node(self):
             return self.head.next
