# Linked Stack

```plantuml
class Node {
  {field} Object data
  {field} Pointer next
  {method} void traverse()
}

class LinkedStack {
  {field} Pointer top
  {method} void push (Object data)
  {method} Object pop()
}

class LinkedList{
  {field} Pointer root
  {method} void append_tail(Object data)
  {method} void append_head(Object data)
  {method} bool search(Object data)
  {method} void traverse()
  {method} void delete(Object data)
  {method} bool empty()
}
Node --|> LinkedList
LinkedList --|> LinkedStack
```

## Reference
::: lists.singly.linked_stack.LinkedStack