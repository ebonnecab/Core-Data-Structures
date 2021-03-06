# from linkedlist import LinkedList
class SetSet:
    def __init__(self, elements=None):
        self.size = 0
        self.elements = list()
        
        if elements is not None:
            for element in elements:
                self.__add__(element)
    
    def __contains__(self, element):
        return True if element in self.elements else False
    
    def __add__(self, element):
        #runtime O(1)
        if not self.__contains__(element):
            self.elements.append(element)
            self.size += 1

    def __remove__(self, element):
        #runtime O(1)
        if self.__contains__(element):
            self.elements.remove(element)
            self.size -= 1
        else:
            raise KeyError('element not found')

    def __union__(self, other_set):
        #runtime O(n) where n is element in set
        for element in other_set.elements:
            if element not in self.elements:
                self.__add__(element)
        
        return self
    
    def __intersection__(self,other_set):
        #runtime O(n * 2) because I loop through both sets
        new_array = []
        for element in self.elements:
            for element in other_set.elements:
                if element in self.elements and element in other_set.elements:
                    new_array.append(element)
        
        return new_array

                
    
    def __difference__(self, other_set):
        #runtime O(n) where n is element in self.elements
        for element in self.elements:
            if element in other_set.elements:
                other_set.__remove__(element)
        
        return other_set
    
    def __is_subset__(self, other_set):
        #runtime O(n * 2) where n is number of elements in set
        subset = []
        for element in self.elements:
            for element in other_set.elements:
                if other_set.__contains__(element):
                    return  True
        return False

