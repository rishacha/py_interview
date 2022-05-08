# Linked Queue

```plantuml
class Node {
  {field} Object data
  {field} Pointer next
  {method} void traverse()
}

class LinkedQueue {
  {method} void enqueue (Object data)
  {method} Object dequeue()
}

class LinkedList{
  {field} Pointer head
  {field} Pointer tail
  {method} void append_tail(Object data)
  {method} void append_head(Object data)
  {method} bool search(Object data)
  {method} void traverse()
  {method} void delete(Object data)
  {method} bool empty()
}
Node --|> LinkedList
LinkedList --|> LinkedQueue
```
## Reference
::: lists.singly.linked_queue.LinkedQueue