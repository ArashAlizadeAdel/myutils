from abc import ABC

class Singleton(ABC):
    '''the singleton object'''
    
    _instance_dict = {}
    def __new__(cls, *args, **kwargs):
        '''The __new__ modified in a way that any object instantiated from
        this class or any of its subclasses, be a singleton of that specific
        class qual name.
        '''
        if cls.__qualname__ not in cls._instance_dict:
            cls._instance_dict[cls.__qualname__] = super().__new__(cls)
        return cls._instance_dict[cls.__qualname__]
