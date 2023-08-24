from abc import ABC,abstractmethod
import copy

class Prototype(ABC):
    '''the prototype object'''
    
    def clone(self):
        '''The method that enables prototyping. It must be implemented by
        the subclass. use super() to implement the default implementation.
        '''
        return copy.deepcopy(self)
