class Queue:
    def __init__(self) -> None:
        self.queue: list[int | float] = []

    def enqueue(self, data: int | float) -> None:
        self.queue.append(data)
        print(f"Enqueued {data}")

    def dequeue(self) -> int | float | None:
        if not self.is_empty():
            removed_data = self.queue.pop(0)
            print(f"Dequeued {removed_data}")
            return removed_data
        else:
            print("Queue is empty. Cannot dequeue.")
            return None

    def peek(self) -> int | float | None:
        if not self.is_empty():
            front_data = self.queue[0]
            print(f"Front item is {front_data}")
            return front_data
        else:
            print("Queue is empty. Nothing to peek.")
            return None

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def display(self) -> None:
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue contents:", " -> ".join(map(str, self.queue)))


def menu() -> None:
    print("\n--- Queue Operations ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Check if Queue is Empty")
    print("5. Display Queue")
    print("6. Exit")


def main() -> None:
    queue = Queue()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter data to enqueue (int or float): ")
            # Convert input to float and then to int if it's a whole number
            try:
                num_data: float = float(data)
                if num_data.is_integer():
                    num_data = int(num_data)
                queue.enqueue(num_data)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            queue.peek()
        elif choice == '4':
            if queue.is_empty():
                print("Queue is empty.")
            else:
                print("Queue is not empty.")
        elif choice == '5':
            queue.display()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
