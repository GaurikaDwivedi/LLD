from solution1 import CircularDeque
def main():
    # Create an instance of CircularDeque with capacity 3
    circular_deque = CircularDeque()
    circular_deque.MyCircularDeque(3)

    # Insert elements at the front
    print("Inserting elements at the front:")
    print("Insert 1:", circular_deque.insertFront(1))  # Returns True
    print("Insert 2:", circular_deque.insertFront(2))  # Returns True
    print("Insert 3:", circular_deque.insertFront(3))  # Returns True
    print("Insert 4:", circular_deque.insertFront(4))  # Returns False (deque is full)

    # Print front and rear
    print("Front:", circular_deque.getFront())  # Returns 3
    print("Rear:", circular_deque.getRear())    # Returns 1

    # Delete elements from the rear
    print("\nDeleting elements from the rear:")
    print("Delete rear:", circular_deque.deleteLast())  # Returns True
    print("Delete rear:", circular_deque.deleteLast())  # Returns True
    print("Delete rear:", circular_deque.deleteLast())  # Returns True
    print("Delete rear:", circular_deque.deleteLast())  # Returns False (deque is empty)

    # Insert elements at the front after deletion
    print("\nInserting elements at the front after deletion:")
    print("Insert 5:", circular_deque.insertFront(5))  # Returns True
    print("Insert 6:", circular_deque.insertFront(6))  # Returns True

    # Print front and rear after insertion
    print("Front:", circular_deque.getFront())  # Returns 6
    print("Rear:", circular_deque.getRear())    # Returns 5

    # Check if the deque is empty and full
    print("\nIs Empty:", circular_deque.isEmpty())  # Returns False
    print("Is Full:", circular_deque.isFull())      # Returns False

if __name__ == "__main__":
    main()
