from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.cache = DoublyLinkedList()
        self.cache_dictionary = dict()
        self.limit = 10

    def __str__(self):
        return "cache: " + str(self.cache) + "\ndictionary: " + str(self.cache_dictionary)

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):

        # key not in dictionary
        if key not in self.cache_dictionary:
            return
        
        # move value to end of list
        # return the requested value
        else:
            existing_node = self.cache_dictionary[key]
            self.cache.move_to_end(existing_node)
            return existing_node.value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):

        # if the key exists in the cache, update the old entry
        if key in self.cache_dictionary:

            # update existing value in existing_node
            existing_node = self.cache_dictionary[key]
            existing_node.value = value
            
            # point to the updated, most-recently-used value
            self.cache.move_to_end(existing_node)

        # key doesn't exist in the cache yet
        else:

            # if the cache is full, remove the least recently used value
            if len(self.cache) == self.limit:
                self.cache.remove_from_head()

            # now that there is a space for the value to go, add it to the most-recently-used spot (tail end)
            # add value to cache. It will be the most recently used value
            self.cache.add_to_tail(value)

            # add the new key to the dictionary.
            self.cache_dictionary[key] = self.cache.tail

# cache = LRUCache(10)
# print(cache, "\n==================\n")
# cache.set('item1', 'a')
# cache.set('item2', 'b')
# cache.set('item2', 'c')
# print(cache)