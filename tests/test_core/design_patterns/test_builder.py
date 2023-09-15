import pytest
import functools
from core.design_patterns.builder import Builder

from .conftest import (inputs_test_builder_basic_functionality,)


pytestmark = [pytest.mark.design_pattern,
              pytest.mark.unit]


@inputs_test_builder_basic_functionality
def test_builder_basic_functionality(_class):
    '''
    A builder takes an object and needed parameters and builds the object through 
    the steps defined in the builder class definition. 
    steps take place in ascending order
    '''
    
    class MyBuilder(Builder):
        
        def step01_task1(self):
            return "task1 done"
        
        def step02_task2(self):
            return "task2 done" 
    
    my_builder = MyBuilder(obj=_class,
                           inputs={"val1" : 1},
                           auto_build=False)
    
    my_builder.build()
    
    assert my_builder.steps_results
    assert "step01_task1" in my_builder.steps_results
    assert "step02_task2" in my_builder.steps_results
    assert my_builder.instance.task1 == "task1 done"
    assert my_builder.instance.task2 == "task2 done"

@inputs_test_builder_basic_functionality
def test_empty_builder_can_do_the_build(_class):
    '''Builder does not care if you provide it with steps or not'''
    
    class MyBuilder(Builder):pass
    
    my_builder = MyBuilder(obj=_class,
                           inputs={"val1" : 1},
                           auto_build=False)
    
    my_builder.build()
    
    assert my_builder.steps_results == {}

@inputs_test_builder_basic_functionality
def test_not_naming_steps(_class):
    '''If you dont name the steps correctly, builder wont recognize them.'''
    
    class MyBuilder(Builder):
        
        def step01(self):
            return "task1 done"
        
        def step02(self):
            return "task2 done" 
    
    my_builder = MyBuilder(obj=_class,
                           inputs={"val1" : 1},
                           auto_build=False)
    
    my_builder.build()
    
    assert my_builder.steps_results == {}
    assert not "step01" in my_builder.steps_results
    assert not "step02" in my_builder.steps_results
    assert not hasattr(my_builder.instance,"step01")
    assert not hasattr(my_builder.instance,"step02")

@inputs_test_builder_basic_functionality
def test_set_auto_build_to_true(_class):
    '''If you set auto_build=True, then the build will take place in instantation'''

    class MyBuilder(Builder):
        
        def step01_task1(self):
            return "task1 done"
        
        def step02_task2(self):
            return "task2 done" 
    
    my_builder = MyBuilder(obj=_class,
                           inputs={"val1" : 1},
                           auto_build=True)
    
    assert my_builder.steps_results
    assert "step01_task1" in my_builder.steps_results
    assert "step02_task2" in my_builder.steps_results
    assert my_builder.instance.task1 == "task1 done"
    assert my_builder.instance.task2 == "task2 done"

class TestDecoratorModification :
    '''You can modify decorate_step method in order to add more
    functionalities to each step. you can also supply neccessary inputs
    in inputs parameter of the builder and then use them when you need to apply
    the decorator.
    '''
    
    @inputs_test_builder_basic_functionality
    def test_add_decorator_after(self,_class):
        '''you can apply decorator after all default decorators'''
    
        class MyBuilder(Builder):
            
            def step01_task1(self):
                return "task1 done"
            
            def step02_task2(self):
                return "task2 done" 
            
            def _some_decorator(self):
                def decorator(func):
                    @functools.wraps(func)
                    def wrapper(*args,**kwargs):
                        result = func(*args,**kwargs)
                        func_name = func.__name__
                        self.some_decorator_applied.append(func_name)
                        return result 
                    return wrapper  
                return decorator   
            
            def decorate_step(self, step):
                step = super().decorate_step(step)
                step = self._some_decorator()(step)
                return step
        
        my_builder = MyBuilder(obj=_class,
                               inputs={"val1" : 1},
                               auto_build=False)
        my_builder.some_decorator_applied = []
        my_builder.build()
        
        assert my_builder.steps_results
        assert "step01_task1" in my_builder.steps_results
        assert "step02_task2" in my_builder.steps_results
        assert my_builder.instance.task1 == "task1 done"
        assert my_builder.instance.task2 == "task2 done"
        assert "step01_task1" in my_builder.some_decorator_applied
        assert "step02_task2" in my_builder.some_decorator_applied

    @inputs_test_builder_basic_functionality
    def test_add_decorator_before(self,_class):
        '''you can apply decorator before all default decorators'''
    
        class MyBuilder(Builder):
            
            def step01_task1(self):
                return "task1 done"
            
            def step02_task2(self):
                return "task2 done" 
            
            def _some_decorator(self):
                def decorator(func):
                    @functools.wraps(func)
                    def wrapper(*args,**kwargs):
                        result = func(*args,**kwargs)
                        func_name = func.__name__
                        self.some_decorator_applied.append(func_name)
                        return result 
                    return wrapper  
                return decorator   
            
            def decorate_step(self, step):
                step = self._some_decorator()(step)
                step = super().decorate_step(step)
                return step
        
        my_builder = MyBuilder(obj=_class,
                               inputs={"val1" : 1},
                               auto_build=False)
        my_builder.some_decorator_applied = []
        my_builder.build()
        
        assert my_builder.steps_results
        assert "step01_task1" in my_builder.steps_results
        assert "step02_task2" in my_builder.steps_results
        assert my_builder.instance.task1 == "task1 done"
        assert my_builder.instance.task2 == "task2 done"
        assert "step01_task1" in my_builder.some_decorator_applied
        assert "step02_task2" in my_builder.some_decorator_applied
    
    @inputs_test_builder_basic_functionality
    def test_add_decorator_with_parameter(self,_class):
        '''you can apply a decorator that needs parameters'''
    
        class MyBuilder(Builder):
            
            def step01_task1(self):
                return "task1 done"
            
            def step02_task2(self):
                return "task2 done" 
            
            def _some_decorator(self,decorator_param):
                def decorator(func):
                    @functools.wraps(func)
                    def wrapper(*args,**kwargs):
                        result = func(*args,**kwargs)
                        func_name = func.__name__
                        self.some_decorator_applied.append(func_name)
                        self.decorator_param_being_found.append(decorator_param)
                        return result 
                    return wrapper  
                return decorator   
            
            def decorate_step(self, step):
                step = self._some_decorator(self.inputs["decorator_param"])(step)
                step = super().decorate_step(step)
                return step
        
        my_builder = MyBuilder(obj=_class,
                               inputs={"val1" : 1,"decorator_param" : 2},
                               auto_build=False)
        my_builder.some_decorator_applied = []
        my_builder.decorator_param_being_found = []
        my_builder.build()
        
        assert my_builder.steps_results
        assert "step01_task1" in my_builder.steps_results
        assert "step02_task2" in my_builder.steps_results
        assert my_builder.instance.task1 == "task1 done"
        assert my_builder.instance.task2 == "task2 done"
        assert "step01_task1" in my_builder.some_decorator_applied
        assert "step02_task2" in my_builder.some_decorator_applied
        assert my_builder.decorator_param_being_found
        assert [i for i in my_builder.decorator_param_being_found if i == 2]

    @inputs_test_builder_basic_functionality
    def test_decorator_can_come_from_outside(self,_class):
        '''extranal decorators can be used for decorating steps'''
    
        def external_decorator(decorator_param):
            def decorator(func):
                @functools.wraps(func)
                def wrapper(*args,**kwargs):
                    result = func(*args,**kwargs)
                    result = decorator_param
                    return result 
                return wrapper  
            return decorator  
    
        class MyBuilder(Builder):
            
            def step01_task1(self):
                return "task1 done"
            
            def step02_task2(self):
                return "task2 done" 
            
            def decorate_step(self, step):
                step = external_decorator(self.inputs["decorator_param"])(step)
                step = super().decorate_step(step)
                return step
        
        my_builder = MyBuilder(obj=_class,
                               inputs={"val1" : 1,"decorator_param" : 2},
                               auto_build=False)
        my_builder.build()
        
        assert my_builder.steps_results
        assert "step01_task1" in my_builder.steps_results
        assert "step02_task2" in my_builder.steps_results
        assert my_builder.instance.task1 == 2
        assert my_builder.instance.task2 == 2
