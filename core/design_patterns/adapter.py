from abc import ABC,abstractmethod
import inspect

class Adapter(ABC):
    
    def __init__(self,obj: object,**kwargs):
        """
        Initialize the Adapter with an object and keyword arguments.
        
        Args:
            obj: The class or callable to be adapted.
            kwargs: Keyword arguments to pass to the object's constructor.
        """
        
        self.params = inspect.signature(obj).parameters.keys()
        self.instance = obj(**{k:v for k,v in kwargs.items() if k in self.params})
    
    def __getattr__(self, attr: str):
        """
        Delegate attribute access to the adapted object.
        
        Args:
            attr: The name of the attribute to access.
        
        Returns:
            The value of the attribute from the adapted object.
        """
        
        return getattr(self.instance, attr)