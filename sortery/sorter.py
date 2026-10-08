import bisect

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class SmartSorter:
    def __init__(self):
        self.lookup = {} 
        
        self.head = None
        self.tail = None

        self.sorted_keys = []

    # main loop
    def feed_list(self, raw_list):
        for item in raw_list:
            self.insert_ordered(item)
    
    # sortery main algorithm
    def insert_ordered(self, value):
        # Handle duplicates
        if value in self.lookup:
            return
            
        new_node = Node(value)

        # empty list (first node)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.lookup[value] = new_node
            self.sorted_keys.append(value)
            return

        
        # find closest lower number
        idx = bisect.bisect_left(self.sorted_keys, value)
                
        if idx > 0:
            closest_lower_val = self.sorted_keys[idx - 1]
            prev_node = self.lookup[closest_lower_val]
            next_node = prev_node.next
            
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = next_node
            
            if next_node:
                next_node.prev = new_node
            else:
                self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.lookup[value] = new_node
        self.sorted_keys.insert(idx, value)

    def get_sorted_list(self):
        sorted_output = []
        current = self.head
        while current:
            sorted_output.append(current.value)
            current = current.next
        return sorted_output
