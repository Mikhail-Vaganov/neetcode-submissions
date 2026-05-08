class Node:
    previous = None
    next = None
    value = None

    def __init__(self, value, previous):
        self.previous = previous
        self.value = value


class LinkedList:
    
    def __init__(self):
        self.Head = None
        self.Tail = None
        self.Length = 0

    
    def get(self, i: int) -> int:
        if i >= self.Length:
            return -1
        elif i == 0:
            return self.Head.value
        else:
            current_node = self.Head
            current_idx = 0
            while(current_node.next):
                current_node = current_node.next
                current_idx += 1
                if current_idx == i:
                    return current_node.value
        return -1
        

    def insertHead(self, val: int) -> None:
        new_node = Node(val, None)
        if not self.Head:
            self.Head = new_node
            self.Tail = self.Head
        else:
            self.Head.previous = new_node
            new_node.next = self.Head
            self.Head = new_node
        self.Length += 1

        

    def insertTail(self, val: int) -> None:
        new_node = Node(val, None)
        if not self.Tail:
            self.Head = new_node
            self.Tail = self.Head
        else:
            self.Tail.next = new_node
            new_node.previous = self.Tail
            self.Tail = new_node
        self.Length += 1

        

    def remove(self, i: int) -> bool:
        node_to_remove = None
        if i >= self.Length:
            return False
        elif i == 0:
            self.Head = self.Head.next
            if self.Head:
                self.Head.previous = None
            else:
                self.Tail = None
            self.Length -= 1
            return True
        elif i == self.Length-1:
            self.Tail = self.Tail.previous
            if self.Tail:
                self.Tail.next = None
            else:
                self.Head = None
            self.Length -= 1
            return True
        else:
            current_node = self.Head
            current_idx = 0
            while(current_node.next):
                current_idx += 1
                current_node = current_node.next
                if current_idx == i:
                    node_to_remove = current_node
                    break
        
        node_to_remove.previous.next = node_to_remove.next
        node_to_remove.next.previous = node_to_remove.previous
        self.Length -= 1
        return True

    def getValues(self) -> List[int]:
        output = []
        if self.Length == 0:
            return output
        else:
            current_node = self.Head
            output.append(current_node.value)
            while(current_node.next):
                current_node = current_node.next
                output.append(current_node.value)
            return output
