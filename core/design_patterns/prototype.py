from abc import ABC,abstractmethod
import copy

class Prototype(ABC):
    '''The prototype object'''
    
    def clone(self):
        '''The method that enables prototyping.'''
        return copy.deepcopy(self)
