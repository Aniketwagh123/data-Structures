from Stack import Stack


def is_balanced(expression: str) -> bool:
    stack = Stack()
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in bracket_pairs.values():
            stack.push(char)
        elif char in bracket_pairs.keys():
            if stack.is_empty():
                return False
            top = stack.pop()
            if bracket_pairs[char] != top:
                return False

    return stack.is_empty()


def main() -> None:
    expression = input("Enter a bracket expression to validate: ")
    if is_balanced(expression):
        print("The brackets are balanced.")
    else:
        print("The brackets are not balanced.")


if __name__ == "__main__":
    main()
