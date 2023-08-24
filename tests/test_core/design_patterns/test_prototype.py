import pytest
import datetime as dt
import time

from core.design_patterns.prototype import Prototype

from .conftest import (inputs_test_prototype_basic_functionality,
                       inputs_test_prototype_advanced_functionality)


pytestmark = [pytest.mark.design_pattern,
              pytest.mark.unit]

@inputs_test_prototype_basic_functionality
def test_prototype_basic_functionality(_class):
    '''
    A prototype object MUST be able to clone itself. Meaning that it can copy
    itself without calling __init__ of the new object being created
    '''
    
    class MyPrototype(Prototype,_class):
        
        def __init__(self):
            self.check_val = dt.datetime.now()
    
    instance1 = MyPrototype()
    time.sleep(0.01)
    instance2 = instance1.clone()
    
    assert instance1 is not instance2
    assert instance1.check_val == instance2.check_val
    assert dir(instance1) == dir(instance2)

@inputs_test_prototype_advanced_functionality
def test_prototype_advanced_functionality(_class):
    '''
    Any object that inherits from Prototype object MUST be able to clone
    itself and not their parents.
    '''
    
    class MyPrototype(Prototype,_class):
        
        def __init__(self):
            self.check_val = dt.datetime.now()
    
    class MyAdvancedPrototype(MyPrototype):
        
        def __init__(self):
            super().__init__()
            self.check_val_advanced = dt.datetime.now()
    
    instance0 = MyPrototype()
    instance1 = MyAdvancedPrototype()
    time.sleep(0.01)
    instance2 = instance1.clone()
    
    assert instance1 is not instance2
    assert instance1.check_val == instance2.check_val
    assert instance1.check_val_advanced == instance2.check_val_advanced
    assert dir(instance1) == dir(instance2)
    assert dir(instance2) != dir(instance0)