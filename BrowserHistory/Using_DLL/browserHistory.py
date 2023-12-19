class Node:

    def __init__(self, outerInstance, url):
        self.url = None
        self.prev = None
        self.next = None

        self._outerInstance = outerInstance

        self.url = url

class BrowserHistory:
    def __init__(self, homepage):

        self.head = Node(self, homepage)
        self.tail = self.head
        self.current = self.head

    def visit(self, url):
        newNode = Node(self, url)
        newNode.next = self.current
        self.current.prev = newNode
        self.head = newNode
        self.current = self.head

    def forward(self, steps):
        node = self.current
        while node.prev is not None and steps > 0:
            node = node.prev
            steps -= 1
        self.current = node
        return node.url

    def back(self, steps):
        node = self.current
        while node.next is not None and steps > 0:
            node = node.next
            steps -= 1
        self.current = node
        return node.url
    
if __name__ == "__main__":
    # Create an instance of BrowserHistory with a homepage URL
    browser = BrowserHistory("https://www.example.com")

    # Visit some URLs
    browser.visit("https://www.example.com/page1")
    browser.visit("https://www.example.com/page2")
    browser.visit("https://www.example.com/page3")

    # Move back and forward in history
    print("Current URL:", browser.current.url)  # Output: https://www.example.com/page3
    print("Back 2 steps:", browser.back(2))    # Output: https://www.example.com/page1
    print("Forward 1 step:", browser.forward(1))  # Output: https://www.example.com/page2
    print("Current URL:", browser.current.url)
    # Add more visits
    browser.visit("https://www.example.com/page4")
    browser.visit("https://www.example.com/page5")

    # Move back and forward again
    print("Current URL:", browser.current.url)  # Output: https://www.example.com/page5
    print("Back 3 steps:", browser.back(3))    # Output: https://www.example.com (assuming there are at least 3 steps to go back)
    print("Current URL:", browser.forward(1)) 