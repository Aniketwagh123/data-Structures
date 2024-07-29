class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Node | None = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def add_at_end(self, data: int) -> None:
        new_node: Node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current: Node = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def add_at_beginning(self, data: int) -> None:
        new_node: Node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_at_position(self, index: int, data: int) -> None:
        if index < 0:
            return
        new_node: Node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current: Node | None = self.head
        position: int = 0
        while current and position < index - 1:
            current = current.next
            position += 1
        if not current:
            return
        new_node.next = current.next
        current.next = new_node

    def search_item(self, data: int) -> int:
        current: Node | None = self.head
        index: int = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def remove_item(self, data: int) -> None:
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current: Node = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def remove_from_end(self) -> None:
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current: Node = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None

    def remove_from_front(self) -> None:
        if not self.head:
            return
        self.head = self.head.next

    def display(self) -> list[int]:
        elements: list[int] = []
        current: Node | None = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements


def menu() -> None:
    print("\n--- Singly Linked List Operations ---")
    print("1. Add item at end")
    print("2. Add item at beginning")
    print("3. Add item at specific position")
    print("4. Search for an item")
    print("5. Remove an item")
    print("6. Remove from end")
    print("7. Remove from front")
    print("8. Display list")
    print("9. Exit")


def main() -> None:
    linked_list: SinglyLinkedList = SinglyLinkedList()

    while True:
        menu()
        choice: str = input("Enter your choice: ")

        if choice == '1':
            data: int = int(input("Enter integer data to add at end: "))
            linked_list.add_at_end(data)
        elif choice == '2':
            data: int = int(input("Enter integer data to add at beginning: "))
            linked_list.add_at_beginning(data)
        elif choice == '3':
            index: int = int(input("Enter position (index) to add item: "))
            data: int = int(input("Enter integer data to add at position: "))
            linked_list.add_at_position(index, data)
        elif choice == '4':
            data: int = int(input("Enter integer data to search: "))
            index: int = linked_list.search_item(data)
            if index != -1:
                print(f"Item found at index {index}")
            else:
                print("Item not found in the list")
        elif choice == '5':
            data: int = int(input("Enter integer data to remove: "))
            linked_list.remove_item(data)
        elif choice == '6':
            linked_list.remove_from_end()
            print("Removed item from end")
        elif choice == '7':
            linked_list.remove_from_front()
            print("Removed item from front")
        elif choice == '8':
            print("Current List:", linked_list.display())
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
