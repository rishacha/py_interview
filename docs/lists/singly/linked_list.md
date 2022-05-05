# Reference

```plantuml
class Node {
  Object data
  Pointer next
  void traverse()
}

class LinkedList{
  Pointer root
  void append()
}
LinkedList <|-- Node
```

::: src.lists.singly.linked_list.LinkedList
    handler: python
    rendering:
      show_root_heading: false
      show_source: false