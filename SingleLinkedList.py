
class SingleLinkedListNode(object):

    def __init__(self,value,nxt):
        self.value = value
        self.next= nxt


class SingleLinkedList(object):

    def __init__(self):
        self.tail = None
        self.head = None

    def push(self,obj):
        node = SingleLinkedListNode(obj,None)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node

        self.tail=node
        return

    def pop(self):
        if self.tail == None:
            return None
        elif self.tail == self.head:
            self.tail = None
            node = self.head
            return node.value
        else:
            node = self.head
            while node.next != self.tail:
                node = node.next
            assert self.tail != node
            self.tail = node
            return node.next.value

    def unshift(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            node = self.head
            self.head = None
            return node.value
        else:
            node = self.head
            node2 = node.next
            self.head = node2
            return node.value

    def remove(self,obj):
        node=SingleLinkedListNode(obj,None)
        curr=self.head
        pre = None
        while curr:
          if curr.value == node.value:
             if pre:
                 if curr.next:
                     pre.next=curr.next
                 else:
                     self.tail = None
             else:
                 self.head=curr.next
             return True
          pre = curr
          curr = curr.next
        return False



    def count(self):
        node = self.head
        count =0
        while node:
            count +=1
            node = node.next
        return count

    def get(self,index):
        met=0
        node = self.head
        while index != met:
            node = node.next
            met +=1
        return node.value



