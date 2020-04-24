class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        '''Inserts the given value into the tree'''

        if self is None:
            self = BinarySearchTree(value)
        else:
            if self.value <= value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)
            else:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)

    def contains(self, target):
        '''
        Returns True if the tree contains the value\n
        False if it does not
        '''

        found = False

        if self is None:
            return False

        if self.value == target:
            return True

        if self.value < target:
            if self.right is None:
                return False
            else:
                found = self.right.contains(target)

        if self.value > target:
            if self.left is None:
                return False
            else:
                found = self.left.contains(target)

        return found
