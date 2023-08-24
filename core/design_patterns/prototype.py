from abc import ABC,abstractmethod
import copy

class Prototype(ABC):
    '''the prototype object'''
    
    def clone(self):
        '''The method that enables prototyping.
        '''
        return copy.deepcopy(self)
