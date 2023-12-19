import collections

class BrowserHistory:

    """Initialization:
The BrowserHistory class is initialized with the homepage URL.
Two deque objects, backHistory and forwardHistory, are created to store the URLs for back and forward navigation.
The homepage is added to the backHistory deque"""

    def __init__(self, homepage):
        self.backHistory = collections.deque([homepage])
        self.forwardHistory = collections.deque([])

    """Visit a URL:
The visit method is called when a user visits a new URL.
The new URL is added to the backHistory deque, and the forwardHistory is cleared since a new visit invalidates the forward history."""

    def visit(self, url):
        self.backHistory.append(url)
        self.forwardHistory.clear()

    """Backward Navigation:
The back method is used to navigate backward by a specified number of steps.
It pops URLs from the backHistory and pushes them to the forwardHistory until the desired number of steps is reached.
The last URL in the backHistory deque is returned."""

    def back(self, steps):
        while steps > 0 and len(self.backHistory) > 1:
            self.forwardHistory.append(self.backHistory.pop())
            steps -= 1
        return self.backHistory[-1]

    """Forward Navigation:
The forward method is used to navigate forward by a specified number of steps.
It pops URLs from the forwardHistory and pushes them back to the backHistory until the desired number of steps is reached.
The last URL in the backHistory deque is returned."""

    def forward(self, steps):
        while steps > 0 and len(self.forwardHistory) > 0:
            self.backHistory.append(self.forwardHistory.pop())
            steps -= 1
        return self.backHistory[-1]

if __name__ == "__main__":
    browser = BrowserHistory("https://www.example.com")

    browser.visit("https://www.example.com/page1")  # backHistory: [home, page1], forwardHistory: []
    browser.visit("https://www.example.com/page2")  # backHistory: [home, page1, page2], forwardHistory: []
    browser.visit("https://www.example.com/page3")  # backHistory: [home, page1, page2, page3], forwardHistory: []

    print("Current URL:", browser.back(2))  # Output: https://www.example.com/page1
    # backHistory: [home, page1], forwardHistory: [page2, page3]

    print("Current URL:", browser.forward(1))  # Output: https://www.example.com/page2
    # backHistory: [home, page1, page2], forwardHistory: [page3]

    browser.visit("https://www.example.com/page4")  # backHistory: [home, page1, page2, page4], forwardHistory: []

    browser.visit("https://www.example.com/page5")  # backHistory: [home, page1, page2, page4, page5], forwardHistory: []

    print("Current URL:", browser.back(3))  # Output: https://www.example.com/page1
    # backHistory: [home, page1], forwardHistory: [page2, page4, page5]

    print("Current URL:", browser.forward(1))  # Output: https://www.example.com/page2
    # backHistory: [home, page1, page2], forwardHistory: [page4, page5]