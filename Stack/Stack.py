class Stack:
    def __init__(self) -> None:
        self.stack: list[int | float | str] = []

    def push(self, data: int | float | str) -> None:
        self.stack.append(data)
        print(f"Pushed {data}")

    def pop(self) -> int | float | str | None:
        if not self.is_empty():
            removed_data = self.stack.pop()
            print(f"Popped {removed_data}")
            return removed_data
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def peek(self) -> int | float | str | None:
        if not self.is_empty():
            top_data = self.stack[-1]
            print(f"Top item is {top_data}")
            return top_data
        else:
            print("Stack is empty. Nothing to peek.")
            return None

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def display(self) -> None:
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack contents:", " -> ".join(map(str, self.stack)))


def menu() -> None:
    print("\n--- Stack Operations ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check if Stack is Empty")
    print("5. Display Stack")
    print("6. Exit")


def main() -> None:
    stack = Stack()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter data to push (int or float): ")
            try:
                num_data: float = float(data)
                if num_data.is_integer():
                    num_data = int(num_data)
                stack.push(num_data)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.peek()
        elif choice == '4':
            if stack.is_empty():
                print("Stack is empty.")
            else:
                print("Stack is not empty.")
        elif choice == '5':
            stack.display()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
