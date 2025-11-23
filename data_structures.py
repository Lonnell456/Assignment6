"""
Assignment 6 – Part 2: Elementary Data Structures

Implements basic:
- ArrayList and Matrix operations
- Stack and Queue using arrays
- Singly linked list

Includes a simple demo in main for screenshots.
"""


class ArrayList:
    """Simple wrapper around Python list to highlight array semantics."""

    def __init__(self):
        self.data = []

    def insert(self, index, value):
        """Insert value at index. Average O(n) due to shifting."""
        self.data.insert(index, value)

    def delete(self, index):
        """Delete and return element at index. O(n) due to shifting."""
        return self.data.pop(index)

    def access(self, index):
        """Return element at index. O(1)."""
        return self.data[index]

    def __repr__(self):
        return f"ArrayList({self.data})"


class Matrix:
    """Simple 2D matrix using a list of lists."""

    def __init__(self, rows, cols, fill=0):
        self.rows = rows
        self.cols = cols
        self.data = [[fill for _ in range(cols)] for _ in range(rows)]

    def set(self, r, c, value):
        """Set element at (r, c). O(1)."""
        self.data[r][c] = value

    def get(self, r, c):
        """Get element at (r, c). O(1)."""
        return self.data[r][c]

    def __repr__(self):
        return "\n".join(str(row) for row in self.data)


class StackArray:
    """Stack implemented on top of Python list."""

    def __init__(self):
        self.data = []

    def push(self, value):
        """Push is amortized O(1)."""
        self.data.append(value)

    def pop(self):
        """Pop is amortized O(1)."""
        if not self.data:
            raise IndexError("pop from empty stack")
        return self.data.pop()

    def peek(self):
        """Return top element without removing it. O(1)."""
        if not self.data:
            raise IndexError("peek from empty stack")
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __repr__(self):
        return f"StackArray({self.data})"


class QueueArray:
    """
    Queue implemented using a list + head index.
    - enqueue: O(1) amortized
    - dequeue: O(1) amortized
    """

    def __init__(self):
        self.data = []
        self.head = 0

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.head >= len(self.data):
            raise IndexError("dequeue from empty queue")
        value = self.data[self.head]
        self.head += 1

        # Occasionally compact the underlying list
        if self.head > 50 and self.head > len(self.data) // 2:
            self.data = self.data[self.head :]
            self.head = 0

        return value

    def is_empty(self):
        return self.head >= len(self.data)

    def __repr__(self):
        return f"QueueArray({self.data[self.head:]})"


class Node:
    """Node for a singly linked list."""

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class SinglyLinkedList:
    """Singly linked list with basic operations."""

    def __init__(self):
        self.head = None

    def insert_front(self, value):
        """Insert new node at the front. O(1)."""
        self.head = Node(value, self.head)

    def delete_front(self):
        """Delete node from the front. O(1)."""
        if self.head is None:
            raise IndexError("delete from empty list")
        value = self.head.value
        self.head = self.head.next
        return value

    def search(self, value):
        """Linear search for value. O(n). Returns index or -1."""
        cur = self.head
        idx = 0
        while cur is not None:
            if cur.value == value:
                return idx
            cur = cur.next
            idx += 1
        return -1

    def to_list(self):
        """Return Python list of all elements. O(n)."""
        result = []
        cur = self.head
        while cur is not None:
            result.append(cur.value)
            cur = cur.next
        return result

    def __repr__(self):
        return f"SinglyLinkedList({self.to_list()})"


def demo():
    """Demo for screenshots and sanity checking."""

    print("=== ArrayList Demo ===")
    arr = ArrayList()
    arr.insert(0, 10)
    arr.insert(1, 20)
    arr.insert(1, 15)
    print("Array after inserts:", arr)
    arr.delete(1)
    print("Array after delete at index 1:", arr)
    print("Access index 1:", arr.access(1))

    print("\n=== Matrix Demo ===")
    m = Matrix(2, 3, fill=0)
    m.set(0, 1, 5)
    m.set(1, 2, 7)
    print("Matrix contents:\n", m)

    print("\n=== Stack Demo ===")
    s = StackArray()
    for i in range(3):
        s.push(i)
    print("Stack after pushes:", s)
    print("Stack pop:", s.pop())
    print("Stack peek:", s.peek())

    print("\n=== Queue Demo ===")
    q = QueueArray()
    for ch in ["A", "B", "C"]:
        q.enqueue(ch)
    print("Queue after enqueues:", q)
    print("Queue dequeue:", q.dequeue())
    print("Queue after one dequeue:", q)

    print("\n=== SinglyLinkedList Demo ===")
    ll = SinglyLinkedList()
    for val in [3, 2, 1]:
        ll.insert_front(val)
    print("Linked list contents:", ll)
    print("Search for 2 -> index:", ll.search(2))
    print("Delete front:", ll.delete_front())
    print("Linked list after delete:", ll)


if __name__ == "__main__":
    demo()
