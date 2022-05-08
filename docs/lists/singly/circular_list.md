# Circular List

```plantuml
class Node {
  {field} Object data
  {field} Pointer next
  {method} void traverse()
}

class CircularList {
  {method} void append_head (Object data)
  {method} void append_tail(Object data)
  {method} void append (Object data)
  {method} bool search(Object data)
  {method} void traverse()
  {method} void delete(Object data)
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
LinkedList --|> CircularList
```

## Reference
::: lists.singly.circular_linked_list.CircularList