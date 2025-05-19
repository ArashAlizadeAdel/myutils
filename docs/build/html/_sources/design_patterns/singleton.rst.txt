===================================
singleton
===================================

Singleton is a design pattern that enforces an object to have only one instance
in the lifetime of a run. If you try to create another instance of that object,
it won't happen and you get the very first instance you created.

In practice, we may want to have multiple singleton objects in our program.
The implementation we provide here, lets us have such functionality.

How it works
==============

#. Import the Singleton class from the package
 
    .. code-block:: python
    
        from core.design_patterns.singleton import Singleton
        
#. Create your own singleton object, with whatever functionality you have in mind

    .. code-block:: python
        
        class MySingleton(Singleton):
            
            def __init__(self,val):
                self.val = val

#. Instantiate the object twice and check if they are the same objects or not. as you can see they are actually the same objects.

    .. code-block:: python
    
        first_instance = MySingleton(val=10)
        second_instance = MySingleton(val=100)

        print(first_instance)  # <__main__.MySingleton object at 0x00000186297EA280>
        print(second_instance) # <__main__.MySingleton object at 0x00000186297EA280>
        print(first_instance.val == second_instance.val) # True
        print(first_instance.val == 100) # True, Initially was 10, but changed to 100 in second instantitation

    .. note::
        
        When a singleton instance is created, no new one can be created afterward. but any change
        to its properities will be applied on the instance. for example
        in the above code, you can see that first_instance.val equals 100; because the second
        instantiation altered this value on the object.

#. Create another singleton object, this newly created object can have singleton feature for its own independently from the first one we created.

    .. code-block:: python
        
        class MyAnotherSingleton(Singleton):
            
            def __init__(self,val):
                self.val = val
        
        third_instance_from_new_object = MyAnotherSingleton(val=200)

        print(first_instance)  # <__main__.MySingleton object at 0x00000186297EA280>
        print(second_instance) # <__main__.MySingleton object at 0x00000186297EA280>
        print(third_instance_from_new_object) # <__main__.MyAnotherSingleton object at 0x00000186297818E0>
        print(first_instance.val == third_instance_from_new_object.val) # False
        print(second_instance.val == third_instance_from_new_object.val) # False

API Reference
==============

.. automodule:: core.design_patterns.singleton
   :members: