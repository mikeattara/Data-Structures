Answer the following questions for each of the data structures you implemented as part of this project.

## Advantages

Advantage of Linked List over Array is that removing item from head or middle Array has to readjust all indices. while it is easier to remove items on linked list from any positin by just adjusting the next and prev

Advantage of Array over Linked List is that searching on Array with index known is faster compared to when we have to loop through each node in linked list.

## Queue

1. What is the runtime complexity of `enqueue`?
   O(1)

2. What is the runtime complexity of `dequeue`?
   O(1)

3. What is the runtime complexity of `len`?
   O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`?

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`?

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
   O(1) - with reference
   O(n) - without reference

2. What is the runtime complexity of `ListNode.insert_before`?
   O(1) - with reference
   O(n) - without reference

3. What is the runtime complexity of `ListNode.delete`?
   O(1) - with reference
   O(n) - without reference

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
   O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
   O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
   O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
   O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
   O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
   O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`?
    O(1) - with reference
    O(n) - without reference
    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    For array, it is always linear. However if the item is the last item, then it is constant time.
    For linked list, it is always constant time if we have reference or linear if we do not have reference
