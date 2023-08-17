from classList import List as SimpleList

class List():

    def __init__(self, criterion, sublist_criterion):
        self.__elements = []
        self.__criterion = criterion
        self.__sublist_criterion = sublist_criterion

    def insert(self, element):

        if len(self.__elements) == 0 or self.comparisonCriterion(element) >= self.comparisonCriterion(self.__elements[-1][0]):
            self.__elements.append([ element, SimpleList(self.__sublist_criterion) ])
        elif self.comparisonCriterion(element) < self.comparisonCriterion(self.__elements[0][0]):
            self.__elements.insert(0, [ element, SimpleList(self.__sublist_criterion) ])
        else:
            index = 1
            while self.comparisonCriterion(element) >= self.comparisonCriterion(self.__elements[index][0]):
                index += 1
            self.__elements.insert(index, [ element, SimpleList(self.__sublist_criterion) ])

    def search(self, search_value, criterion = None):
        position = None

        first = 0
        last = self.size() - 1

        while (first <= last and position == None):
            middle = (first + last) // 2

            if search_value == self.comparisonCriterion(self.__elements[middle][0], criterion):
                position = middle
            elif search_value > self.comparisonCriterion(self.__elements[middle][0], criterion):
                first = middle + 1
            else:
                last = middle - 1

        return position

    def delete(self, value):
        position = self.search(value)
        deleted_value = None

        if position:
            deleted_value = self.__elements.pop(position)

        return deleted_value

    def size(self):
        return len(self.__elements)

    def iteration(self):
        for value in self.__elements:
            print(value[0])
            print('========= Sublist =========')
            value[1].iteration()

    def getByValue(self, value):
        position = self.search(value)
        gotten_element = None

        if position:
            gotten_element = self.__elements[position]

        return gotten_element

    def getByIndex(self, index):
        gotten_element = None

        if (index >= 0 and index < self.size()):
            gotten_element = self.__elements[index]

        return gotten_element

    def set(self, value, newValue):
        position = self.search(value)

        if position is not None:
            value = self.delete(value)
            self.insert(newValue)

    def comparisonCriterion(self, element, opcionalCriterion = None):

        criterion = opcionalCriterion if opcionalCriterion else self.__criterion

        if isinstance(element, (int, str, bool)):
            return element
        else:
            dictionary = element.__dict__

            if criterion in dictionary:
                return dictionary[criterion]
            else:
                return('No se puede ordenar por este criterio')

    def orderBy(self, opcionalCriterion = None, reverse = False):
        dictionary = self.__elements[0][0].__dict__

        criterion = opcionalCriterion if opcionalCriterion else self.__criterion

        if criterion in dictionary:
            def criterionFunction(value):
                return value.__dict__[criterion]

            self.__elements.sort(key = criterionFunction, reverse = reverse)
        else:
            print('No se puede ordenar por este criterio')