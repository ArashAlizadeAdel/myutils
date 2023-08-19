import pytest

from core.design_patterns.singleton import SingletonObject

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
    class MySingletonObject(SingletonObject,_class):
        pass
    
    try :
        instance1 = MySingletonObject(val1=1)
    except TypeError:
        instance1 = MySingletonObject()
    
    try :
        instance2 = MySingletonObject(val1=2)
    except TypeError:
        instance2 = MySingletonObject()
    
    assert instance1 is instance2

@inputs_test_multiple_singleton_functionality
def test_multiple_singleton_functionality(_class):
    '''
    Different Singleton objects MUST be independent of each other
    '''
    class MySingletonObject(SingletonObject,_class):
        pass
    
    class MyAnotherSingletonObject(SingletonObject,_class):
        pass
    
    try :
        instance1 = MySingletonObject(val1=1)
    except TypeError:
        instance1 = MySingletonObject()
    
    try :
        instance2 = MyAnotherSingletonObject(val1=2)
    except TypeError:
        instance2 = MyAnotherSingletonObject()
    
    assert instance1 is not instance2
    
    if hasattr(instance1,'val1') :
        assert instance1.val1 != instance2.val1

@inputs_test_singleton_attrs_can_change_during_duplicate_instantiation
def test_singleton_attrs_can_change_during_duplicate_instantiation(_class):
    '''
    Another Instantiation of a singleton object that has attributes to initilize,
    impacts the very first attributes of the singleton object
    '''
    class MySingletonObject(SingletonObject,_class):
        pass
    
    try :
        instance1 = MySingletonObject(val1=1)
    except TypeError:
        instance1 = MySingletonObject()
    
    try :
        instance2 = MySingletonObject(val1=2)
    except TypeError:
        instance2 = MySingletonObject()
    
    assert instance1 is instance2
    
    if hasattr(instance1,'val1') :
        assert instance1.val1 == instance2.val1
        assert instance1.val1 == 2
        assert instance2.val1 == 2