import random
import time
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
    def feed_unorganized_list(self, raw_list):
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








if __name__ == "__main__":
    random.seed(42)
    messy_list = random.sample(range(0, 1000000), 1000000)
    
    print("--- TESTING YOUR SCRIPT WITH 1,000 VALUES ---")
    print("First 10 completely unorganized inputs entering your system:")
    print(messy_list[:10], "...\n")
    
    # 2. Instantiate and time your custom sorter execution
    sorter = SmartSorter()
    
    start_time = time.time()
    sorter.feed_unorganized_list(messy_list)
    end_time = time.time()
    
    # 3. Pull the organized data out
    sorted_result = sorter.get_sorted_list()
    
    # 4. Verify structural accuracy against Python's native quicksort algorithm
    is_correct = (sorted_result == sorted(messy_list))
    
    # 5. Output metrics
    print(f"Extraction Successful! Total items processed: {len(sorted_result)}")
    print("First 10 perfectly sorted outputs leaving your system:")
    print(sorted_result[:10], "...\n")
    
    print(f"Is your custom logic 100% accurate? -> {is_correct}")
    print(f"Total time taken to sort the chaos: {end_time - start_time:.4f} seconds")

