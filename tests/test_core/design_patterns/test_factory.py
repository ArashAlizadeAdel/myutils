import pytest

from core.design_patterns.factory import Factory

from .conftest import (inputs_test_factory_basic_functionality,)


pytestmark = [pytest.mark.design_pattern,
              pytest.mark.unit]

class TestFactory:
    '''
    A factory object is responsible for seperating object instantiation from
    the rest of the code.
    '''
    
    @inputs_test_factory_basic_functionality
    def test_build_object(self,_class):
        '''
        A factory must be able to take an object mapper and instantiate mapped items 
        by their names.
        Also an undefined object cannot be instantiated and an error must be raised.
        '''
        
        class MyFactory(Factory):pass
        
        class MyObject1(_class):pass
        class MyObject2(_class):pass
        
        objects = {"my_object1" : MyObject1,"my_object2" : MyObject2}
        
        factory_instance = MyFactory(objects=objects)
        
        for obj in objects:
            try :
                instance = factory_instance.build_object(obj,params={"val1" : 1})
            except TypeError:
                instance = factory_instance.build_object(obj)
                
            assert isinstance(instance,objects[obj])
        
        with pytest.raises(Exception) :
            factory_instance.build_object("undefined_object")

    @inputs_test_factory_basic_functionality
    def test_add_object(self,_class):
        '''
        You can add an object to the factory.
        on_duplicate parameter determines the behaviour in the case.
        '''
        
        class MyFactory(Factory):pass
        
        class MyObject1(_class):pass
        class MyObject2(_class):pass
        
        objects = {"my_object1" : MyObject1}
        
        factory_instance = MyFactory()
        factory_instance.add_object(name="my_object1", obj=objects["my_object1"])
        
        for obj in objects:
            try :
                instance = factory_instance.build_object(obj,params={"val1" : 1})
            except TypeError:
                instance = factory_instance.build_object(obj)
                
            assert isinstance(instance,objects[obj])
        

        factory_instance.add_object(name="my_object1",obj=MyObject2,on_duplicate="skip")
        try :
            instance = factory_instance.build_object("my_object1",params={"val1" : 1})
        except TypeError:
            instance = factory_instance.build_object("my_object1")
        assert not isinstance(instance,MyObject2)

        factory_instance.add_object(name="my_object1",obj=objects["my_object1"],on_duplicate="replace")

    @inputs_test_factory_basic_functionality
    def test_add_objects(self,_class):
        '''
        You can add multiple objects to the factory.
        on_duplicate parameter determines the behaviour in the case.
        '''
        
        class MyFactory(Factory):pass
        
        class MyObject1(_class):pass
        class MyObject2(_class):pass
        
        objects = {"my_object1" : MyObject1,"my_object2" : MyObject2}
        
        factory_instance = MyFactory()
        factory_instance.add_objects(objects=objects)
        
        for obj in objects:
            try :
                instance = factory_instance.build_object(obj,params={"val1" : 1})
            except TypeError:
                instance = factory_instance.build_object(obj)
                
            assert isinstance(instance,objects[obj])
        

        factory_instance.add_objects(objects=objects,on_duplicate="skip")
        factory_instance.add_objects(objects=objects,on_duplicate="replace")
    
    @inputs_test_factory_basic_functionality
    def test_delete_object(self,_class):
        '''
        You can delete an already defined object. duplicate deletion is also safe.
        '''
        
        class MyFactory(Factory):pass
        
        class MyObject1(_class):pass
        
        objects = {"my_object1" : MyObject1}
        
        factory_instance = MyFactory(objects)
        
        factory_instance.delete_object("my_object1")
        factory_instance.delete_object("my_object1")
        
        assert "my_object1" not in factory_instance.objects

    @inputs_test_factory_basic_functionality
    def test_delete_objects(self,_class):
        '''
        You can delete already defined objects. duplicate deletion is also safe.
        '''
        
        class MyFactory(Factory):pass
        
        class MyObject1(_class):pass
        class MyObject2(_class):pass
        
        objects = {"my_object1" : MyObject1,
                   "my_object2" : MyObject2,
                   }
        
        factory_instance = MyFactory(objects)
        
        factory_instance.delete_objects(list(objects.keys()))
        factory_instance.delete_objects(list(objects.keys()))
        
        for key in objects.keys():
            assert key not in factory_instance.objects