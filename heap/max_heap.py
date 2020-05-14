import math

class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        pass

    def delete(self):
        pass

    def get_max(self):

        if len(self.storage) > 0:
            return self.storage[0]
        else:
            return None

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):

        parent_index = math.floor((index - 1) / 2)
        parent_value = self.storage[parent_value]

        current_value = self.storage[index]

        # move the larger value higher
        if parent_value < current_value:
            self.storage[parent_index] = current_value
            self.storage[index] = parent_value

    def _sift_down(self, index):
        
        parent_value = self.storage[index]

        child1_index = 2 * index
        child1_value = self.storage[child1_index]

        child2_index = child1_index + 1
        child2_value = self.storage[child2_index]

        larger_child_index = child1_index if child1_value > child2_value else child2_index
        larger_child_value = self.storage[larger_child_index]

        # move the larger value higher
        if parent_value < larger_child_value:
            self.storage[index] = larger_child_value
            self.storage[larger_child_index] = parent_value