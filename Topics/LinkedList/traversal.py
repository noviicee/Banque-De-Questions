from email import header


class LinkedList:
    def __init__(self) -> None:
        self.head=None
        self.data=None
    def addToList(self, data):
        #add to front
        if self.head is None:
            self.head=