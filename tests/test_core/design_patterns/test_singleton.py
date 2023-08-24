import pytest

from core.design_patterns.singleton import Singleton

from .conftest import (inputs_test_multiple_singleton_functionality,
                       inputs_test_singleton_attrs_can_change_during_duplicate_instantiation,
                       inputs_test_singleton_basic_functionality)


pytestmark = [pytest.mark.design_pattern,
              pytest.mark.unit]

@inputs_test_singleton_basic_functionality
def test_singleton_basic_functionality(_class):
    '''
    Multiple instantiation of a singleton object MUST end with existance of only
    the first instance
    '''
    class MySingleton(Singleton,_class):
        pass
    
    try :
        instance1 = MySingleton(val1=1)
    except TypeError:
        instance1 = MySingleton()
    
    try :
        instance2 = MySingleton(val1=2)
    except TypeError:
        instance2 = MySingleton()
    
    assert instance1 is instance2

@inputs_test_multiple_singleton_functionality
def test_multiple_singleton_functionality(_class):
    '''
    Different Singleton objects MUST be independent of each other
    '''
    class MySingleton(Singleton,_class):
        pass
    
    class MyAnotherSingleton(Singleton,_class):
        pass
    
    try :
        instance1 = MySingleton(val1=1)
    except TypeError:
        instance1 = MySingleton()
    
    try :
        instance2 = MyAnotherSingleton(val1=2)
    except TypeError:
        instance2 = MyAnotherSingleton()
    
    assert instance1 is not instance2
    
    if hasattr(instance1,'val1') :
        assert instance1.val1 != instance2.val1

@inputs_test_singleton_attrs_can_change_during_duplicate_instantiation
def test_singleton_attrs_can_change_during_duplicate_instantiation(_class):
    '''
    Another Instantiation of a singleton object that has attributes to initilize,
    impacts the very first attributes of the singleton object
    '''
    class MySingleton(Singleton,_class):
        pass
    
    try :
        instance1 = MySingleton(val1=1)
    except TypeError:
        instance1 = MySingleton()
    
    try :
        instance2 = MySingleton(val1=2)
    except TypeError:
        instance2 = MySingleton()
    
    assert instance1 is instance2
    
    if hasattr(instance1,'val1') :
        assert instance1.val1 == instance2.val1
        assert instance1.val1 == 2
        assert instance2.val1 == 2