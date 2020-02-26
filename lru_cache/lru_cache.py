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
        self.limit = limit
        self.size = 0
        self.list = DoublyLinkedList()
        self.cache = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # if the key exists in the cache dictionary
        if key in self.cache:
            # get the value
            recently_accessed = self.cache[key]
            # move it to the front of the list and make it the head
            self.list.move_to_front(recently_accessed)
            # then return the value of the head
            return self.list.head.value[1]
        else:
            return None

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
        # edge case: if key already exists, simply move it to front
        if key in self.cache:
            self.list.move_to_front(self.cache[key])
            # add the (key, value) pair to the head
            self.list.head.value = (key, value)
            # overwrite storage value if applicable
            self.cache[key] = self.list.head
        else:
            self.list.add_to_head((key, value))
            self.size += 1
            self.cache[key] = self.list.head
        if self.size > self.limit:
            # find the least accessed (key,value) pair - at the tail of the DLL
            least_accessed = self.list.tail.value[0]
            # delete the key
            del self.cache[least_accessed]
            # remove from tail of the list as well
            self.list.remove_from_tail()
            # then decrement the size
            self.size -= 1
