class Bag:
    def __init__(self):
        self.bag = []
    def insert(self, e):
        self.bag.append(e)
    def remove(self, e):
        self.bag.remove(e)
    def contain(self, e):
        if e in self.bag:
            return True
        else:
            return False
    def count():
        return len(self.bag)