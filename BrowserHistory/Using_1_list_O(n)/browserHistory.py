class BrowserHistory:
    def __init__(self, homepage):
        self.visitedWebpages = []
        self.visitedWebpages.append(homepage)
        self.currentIndex = 0

    def visit(self, url):
        self.currentIndex += 1
        if self.currentIndex <= len(self.visitedWebpages) - 1:
            self.visitedWebpages[self.currentIndex] = url
        else:
            self.visitedWebpages.append(url)
        self.visitedWebpages[self.currentIndex + 1: len(self.visitedWebpages)].clear()

    def back(self, steps):
        self.currentIndex = max(0, self.currentIndex - steps)
        return self.visitedWebpages[self.currentIndex]

    def forward(self, steps):
        self.currentIndex = min(len(self.visitedWebpages) - 1, self.currentIndex + steps)
        return self.visitedWebpages[self.currentIndex]
    
if __name__ == "__main__":
    browser = BrowserHistory("https://www.example.com")

    browser.visit("https://www.example.com/page1")  # currentIndex: 1, visitedWebpages: [home, page1]
    browser.visit("https://www.example.com/page2")  # currentIndex: 2, visitedWebpages: [home, page1, page2]
    browser.visit("https://www.example.com/page3")  # currentIndex: 3, visitedWebpages: [home, page1, page2, page3]

    print("Current URL:", browser.back(2))  # Output: https://www.example.com/page1
    # currentIndex: 1, visitedWebpages: [home, page1, page2, page3]

    print("Current URL:", browser.forward(1))  # Output: https://www.example.com/page2
    # currentIndex: 2, visitedWebpages: [home, page1, page2, page3]

    browser.visit("https://www.example.com/page4")  # currentIndex: 3, visitedWebpages: [home, page1, page2, page4]
    browser.visit("https://www.example.com/page5")  # currentIndex: 4, visitedWebpages: [home, page1, page2, page4, page5]

    print("Current URL:", browser.back(3))  # Output: https://www.example.com (assuming there are at least 3 steps to go back)
    # currentIndex: 1, visitedWebpages: [home, page1, page2, page4, page5]

    print("Current URL:", browser.forward(1))  # Output: https://www.example.com/page2
    # currentIndex: 2, visitedWebpages: [home, page1, page2, page4, page5]