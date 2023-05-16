class Stack():
    """Stack class"""

    def __init__(self):
        self.__elements = []
    
    def __eq__(self, stack_aux):
        if isinstance(stack_aux, Stack):
            return self.__elements == stack_aux.__elements
        else:
            return False
    
    # Methods
    def push(self, value):
        self.__elements.append(value)
    
    def pop(self):
        if self.size() > 0:
            return self.__elements.pop()

    def size(self):
        return len(self.__elements)

    def on_top(self):
        if self.size() > 0:
            return self.__elements[-1]