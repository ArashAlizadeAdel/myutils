from abc import ABC
from typing import Dict, Any

class Factory(ABC):
    '''The factory object. This object implements a practical factory method'''
    
    def __init__(self,objects : Dict[str, object] = dict()):
        
        self.objects = objects
    
    def build_object(self,name : str,params : Dict[str, Any] = dict()) -> object:
        '''Builds the requested object; If any paramter is required for instantiation
        they must be passed in.
        '''
        
        obj = self.objects.get(name)
        if obj :
            instance = obj(**params)
        else :
            raise Exception(f"name requested is not defined, name : {name}")
        return instance
    
    def add_object(self,name : str, obj : object,on_duplicate : str = "replace") -> None:
        '''Adds an object to objects while considering on_duplicate behaviour'''
        
        if (on_duplicate == "skip") and (name in self.objects) :
            pass
        else :
            self.objects[name] = obj

    def add_objects(self, objects : Dict[str, object], on_duplicate : str = "replace") -> None:
        '''Adds multiple objects to objects while considering on_duplicate behaviour'''
        
        for obj in objects:
            self.add_object(obj, objects[obj],on_duplicate=on_duplicate)

    def delete_object(self,name : str) -> None:
        '''Deletes an object from objects'''
        
        self.objects.pop(name,None)
        
    def delete_objects(self, objects : list) -> None:
        '''Deletes Multipe objects from objects'''
        
        for obj in objects:
            self.delete_object(obj)