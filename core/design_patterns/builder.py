from typing import Dict, Any, List, Callable
import re
import inspect
from abc import ABC
import functools

class Builder(ABC):
    _steps_pattern = r'^step\d+_.'
    
    def __init__(self,obj : object,inputs : Dict[str,Any] = dict(),auto_build : bool = True):
        self.inputs = inputs
        self.params = list(inspect.signature(obj).parameters.keys())
        self.instance = obj(**{k:v for k,v in inputs.items() if k in self.params})
        self.steps_results = dict()
        if auto_build:self.build()
    
    def _add_to_step_results_decorator(self):
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
        step = self._add_to_step_results_decorator()(step)
        step = self._add_to_instance_decorator()(step)
        return step
    
    def build(self):
        steps = [i for i in dir(self) if re.match(self._steps_pattern,i)]
        steps.sort()
        for step in steps:
            step = getattr(self,step)
            step = self.decorate_step(step)
            step()