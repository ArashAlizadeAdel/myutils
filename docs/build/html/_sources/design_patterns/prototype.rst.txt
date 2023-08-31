===================================
prototype
===================================

Prototype is a design pattern that lets an object, be able to create copies
of itself with a method named **clone**.

This is particularly useful when you want to instantiate an object multiple times
but you don't want to call the codes in __init__() of the class.
for example there maybe a call to an API, or connection to a database that you want to avoid
to happen for multiple times.

How it works
==============

#. Import the Prototype class from the package
 
    .. code-block:: python
    
        from core.design_patterns.prototype import Prototype
        
#. Create a prototype object, and put a print statement in the __init__()

    .. code-block:: python
        
        class MyPrototype(Prototype):
            
            def __init__(self,val):
                self.val = val
                print("prototype object instantiated with value {0}".format(val))

#. Instantiate the object and you see the print statement goes off.

    .. code-block:: python
    
        instance = MyPrototype(val=10) # prototype object instantiated with value 10

#. Now create a copy of this instance using **clone** method. You can also overwrite this method if needed.

    .. code-block:: python
        
        copied_instance = instance.clone()
    
    as you see, no print statement executed, meaning that the __init__() method didnt get called.
    you copied the instance with all of its attributes.

API Reference
==============

.. automodule:: core.design_patterns.prototype
   :members: