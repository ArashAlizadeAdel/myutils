from typing import Dict, Any, List, Callable
import re
import inspect
from abc import ABC
import functools

class Builder(ABC):
    '''The builder object. This object implements a practical builder design pattern'''
    
    _steps_pattern = r'^step\d+_.'
    
    def __init__(self,obj : object,inputs : Dict[str,Any] = dict(),auto_build : bool = True):
        '''Builder takes an object and its parameters. Creates an instance of that object
        if auto_build is set to True, all the steps to build the instance takes place.
        In case that you add more decorators to the builder and those decorators
        have inputs, you must include them in inputs.
        '''
        
        self.inputs = inputs
        self.params = list(inspect.signature(obj).parameters.keys())
        self.instance = obj(**{k:v for k,v in inputs.items() if k in self.params})
        self.steps_results = dict()
        if auto_build:self.build()
    
    def _add_to_step_results_decorator(self):
        '''step_results is a dict. any of the steps being ran, their results
        must be gathered in this dict.
        '''
        
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kwargs):
                result = func(*args,**kwargs)
                func_name = func.__name__
                self.steps_results[func_name] = result
                return result 
            return wrapper  
        return decorator   

    def _add_to_instance_decorator(self):
        '''each step being ran must be added as an attribute to the object instance.
        attribute name will not have the "steps" part of the function name;
        for example an step named "step1_something" will be an attribute named
        "something" on the instance.
        '''
        
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kwargs):
                result = func(*args,**kwargs)
                func_name = func.__name__
                func_name = re.sub(self._steps_pattern[:-1], "", func_name)
                setattr(self.instance,func_name,result)
                return result 
            return wrapper  
        return decorator  
    
    def decorate_step(self,step : Callable[[],Any]):
        '''Steps need to be decorated. if you need to add more decorators,
        extend this method.
        '''
        step = self._add_to_step_results_decorator()(step)
        step = self._add_to_instance_decorator()(step)
        return step
    
    def build(self):
        '''When the build is being called, steps will take place and build
        the target instance.
        '''
        steps = [i for i in dir(self) if re.match(self._steps_pattern,i)]
        steps.sort()
        for step in steps:
            step = getattr(self,step)
            step = self.decorate_step(step)
            step()