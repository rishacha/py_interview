# Linked List

### Class diagram
```plantuml
class Node {
  {field} Object data
  {field} Pointer next
  {method} void traverse()
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
```

::: lists.singly.linked_list.LinkedList