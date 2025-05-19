===================================
factory
===================================

Factory is a design pattern that helps us seperate instantiation of an object
from its usage. Defining such interface has following benefits :

* we can extend our code more easily, simply adding new objects to the factory
* we can switch the object responsible for instantiation in runtime
* we can develop more dynamic programs

There are two variations of the factory pattern. **Factory Method** and **Abstract Factory Pattern**.
The implementation we provide here is inspired by **Factory Method**.

How it works
==============

#. Import the Factory class from the package
 
    .. code-block:: python
    
        from core.design_patterns.factory import Factory
        
#. Create some fruit objects and then put them in a mapper alongside with their titles. then create a FruitFactory that inherits from "Factory" we imported earlier.then create an instance of the factory and pass the objects mapper to it.

    .. code-block:: python
        
        class Apple:
            def __str__(self):
                return "this is an apple"
        
        class Orange:
            def __str__(self):
                return "this is a orange"
        
        class Banana:
            def __str__(self):
                return "this is a banana"
        
        objects = {"apple" : Apple, "orange" : Orange, "banana" : Banana}
        
        class FruitFactory(Factory):pass
        
        fruit_factory = FruitFactory(objects=objects)

#. This **fruit_factory** now can generate fruits that we want using :class:`~core.design_patterns.factory.Factory.build_object` method; we just need to ask it by the title. The important point here is that we are not going to directly instantiate fruits; the factory will handle it.

    .. code-block:: python
    
        apple_instance1 = fruit_factory.build_object("apple")
        print(apple_instance1) #this is an apple

#. There will be cases that the object needs parameters to get instantiated. In this case we pass those parameters to :class:`~core.design_patterns.factory.Factory.build_object` method.

    .. code-block:: python
    
        class Lemon :
            
            def __init__(self,color):
                self.color = color
    
            def __str__(self):
                return f"this is a {self.color} lemon"
        
        fruit_factory.add_object("lemon", Lemon)
        lemon_instance = fruit_factory.build_object("lemon",{"color" : "green"})
        print(lemon_instance) #this is a green lemon

#. As you see, we can add objects to our factory using :class:`~core.design_patterns.factory.Factory.add_object` and :class:`~core.design_patterns.factory.Factory.add_objects`.

    .. code-block:: python

        class Pineapple :
            def __str__(self):
                return "this is a pineapple"
    
        class Coconut :
            def __str__(self):
                return "this is a coconut"
    
        fruit_factory.add_object("pineapple", Pineapple)
        fruit_factory.add_objects({"pineapple": Pineapple, "coconut" : Coconut})
        
    .. note::
        You may have noticed that pineapple was added twice in our example. The behaviour
        for adding duplicate items can be changed with on_duplicate parameter. There are
        two options : **replace** and **skip**. the default is **replace**.

#. We can also delete objects from our factory using :class:`~core.design_patterns.factory.Factory.delete_object` and :class:`~core.design_patterns.factory.Factory.delete_objects`.

    .. code-block:: python
    
        fruit_factory.delete_object("pineapple")
        fruit_factory.delete_objects(["pineapple","coconut"])
        print([k for k in fruit_factory.objects.keys()]) #['apple', 'orange', 'banana', 'lemon']

.. hint::
    It is recommended to add similar objects with same interfaces to a factory.
    This way you can write more dynamic codes and benefit from ducktyping when it comes to parameters.

API Reference
==============

.. automodule:: core.design_patterns.factory
   :members: