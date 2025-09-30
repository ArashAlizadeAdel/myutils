===================================
builder
===================================
Builder is a design pattern that enables creating an object from a complex process.
This design is usually represented by 2 objects; builder and director. director
is the object that knows the process while builder is the object that has the steps
of the process. In our implementation it is different; Builder itself knows how
to build the object and doesn't need the director.
Each step of the process will
be defined on the builder (with a specific naming convention) and those steps get ran in order
when you execute :class:`~core.design_patterns.builder.Builder.build` method.


How it works
==============

Imagine you are running a burger shop, where each burger is made step-by-step,
following specific recipes. Some customers want a simple burger, 
while others may want some other variations.
To manage this process efficiently, we use a Burger Builder that constructs burgers 
dynamically, step by step, based on the customer's order.

This analogy demonstrates the Builder Design Pattern in action,
where the process of building an object (in this case, a burger)
is broken down into sequential steps.
Each step adds a specific ingredient or attribute to the final product.

#. Import the Builder class from the package

    .. code-block:: python
    
        from core.design_patterns.builder import Builder

#. Define the Burger object. This class represents the final product that we are building. It has attributes like name and price, and additional attributes may added dynamically during the building process.

    .. code-block:: python
    
        class Burger:
            def __init__(self, name, price):
                self.name = name
                self.price = price
    
            def __str__(self):
                attributes = ", ".join(f"{key}: {value}\n" for key, value in self.__dict__.items())
                return f"Burger Ready To Deliver : \n({attributes})"

#. Define the BurgerBuilder object.This class is like the chef in your burger shop. It knows the recipe and follows a series of steps to create the burger. Steps are executed sequentially to construct the burger. The naming convention (stepX_<name>) ensures that the steps are executed in the correct order.

    .. code-block:: python

        class BurgerBuilder(Builder) :
            
            def step01_add_bread(self):
                return "Simple Bread Added."
            
            def step02_add_patty(self):
                return "Meat Patty Added"
            
            def step03_add_cheese(self):
                return "No Cheese Added"
            
            def step04_add_veggies(self):
                return "Base Veggies Added"
            
            def step05_add_suaces(self):
                return "Ketchup suace Added"

#. Now we have the blue print to build burgers. We can inherit from our BurgerBuilder to define different types of burgers.

    .. code-block:: python
    
        class SimpleBurgerBuilder(BurgerBuilder):pass
    
        class DoubleCreamyCheeseBurgerBuilder(BurgerBuilder) :
            
            def step03_add_cheese(self):
                return "Double Layer of Chedar Cheese Added"
            
            def step05_add_suaces(self):
                return "Ketchup suace and Sour Cream Added"

#. We are ready to build burgers for our customers! we use our builders in a Dictionary as menu :

    .. code-block:: python

        menu = [
            {"id" : 1 ,"name" : "Simple Burger","price" : 10, "builder" : SimpleBurgerBuilder},
            {"id" : 2 ,"name" : "Double Cheese Creamy Burger","price" : 17, "builder" : DoubleCreamyCheeseBurgerBuilder},
            ]

#. A customer view the menu and submit orders :

    .. code-block:: python
    
        customer_orders = [ {"id" : 1 , "count" : 5},
                           {"id" : 2 , "count" : 3}
                          ]

#. Based on these orders, We have to make 8 burgers. For each order we run its corresponding Builder N times based on "count" value :

    .. code-block:: python
    
        deliverables = []
        for order in customer_orders :
        
            for i in range(order["count"]) :
            
                item = [i for i in menu if i["id"] == order["id"]][0] # select customer's order from the menu
                item_materialized = item["builder"](Burger,item) # build the selected menu item
        
                # finalize the order as a deliverable
                
                deliverable = {}
                deliverable["burger_as_string"] = str(item_materialized.instance)
                deliverable["burger_as_instance"] = item_materialized.instance
                
                deliverables.append(deliverable)

#. Burgers are ready. We can utilize them as we wish. For example we may want to calculate the order price :

    .. code-block:: python
    
            order_price = sum([i["burger_as_instance"].price for i in deliverables]) # 101 dollars


#. Now Imagine the manager wants to measure preparation time of each burger being built. How can we achieve this goal in an efficient way? The answer is that our Builder object accepts decorators. we can define them on the class or outside of it and apply them on every step. here we define a simple decorator that measures the duration of the run.
    
        .. note::
            after defining the decorator, you have to also extend the method **decorate_step** to apply the decorator to the runtime.

    .. code-block:: python    
    
        class BurgerBuilder(Builder) :
            
            def step01_add_bread(self):
                return "Simple Bread Added."
            
            def step02_add_patty(self):
                return "Meat Patty Added"
            
            def step03_add_cheese(self):
                return "No Cheese Added"
            
            def step04_add_veggies(self):
                return "Base Veggies Added"
            
            def step05_add_suaces(self):
                return "Ketchup suace Added"
            
            # the decorator defined on the builder    
            def _duration_decorator(self):
                '''Evaluate duration to prepare the burger.'''
                
                def decorator(func):
                    @functools.wraps(func)
                    def wrapper(*args,**kwargs):
                        start_time = dt.datetime.now()
                        result = func(*args,**kwargs)
                        end_time = dt.datetime.now()
                        duration = (end_time - start_time).total_seconds()
                        
                        if not hasattr(self, "duration") :
                            self.duration = 0
                            
                        self.duration += duration
                        
                        return result 
                    return wrapper  
                return decorator
            
            # the decorator applied on each step
            def decorate_step(self, step):
                step = super().decorate_step(step)
                step = self._duration_decorator()(step)
                return step

#. Then for demonstration purposes we add some sleep to our steps so we can have numbers as the preparation duration.

    .. code-block:: python   
    
        class DoubleCreamyCheeseBurgerBuilder(BurgerBuilder) :
            
            def step03_add_cheese(self):
                time.sleep(random.randint(1,3))
                return "Double Layer of Chedar Cheese Added"
            
            def step05_add_suaces(self):
                time.sleep(random.randint(2,4))
                return "Ketchup suace and Sour Cream Added"

#. The duration is defined on the builder instance, not the burger instance. so we add it to our delivarables :

    .. code-block:: python
    
        deliverables = []
        for order in customer_orders :
        
            for i in range(order["count"]) :
            
                item = [i for i in menu if i["id"] == order["id"]][0] # select customer's order from the menu
                item_materialized = item["builder"](Burger,item) # build the selected menu item
        
                # finalize the order as a deliverable
                
                deliverable = {}
                deliverable["burger_as_string"] = str(item_materialized.instance)
                deliverable["burger_as_instance"] = item_materialized.instance
                deliverable["duration"] = item_materialized.duration # duration added
                
                deliverables.append(deliverable)
    
#. Now we can easily measure the preparation_time.

    .. code-block:: python

        total_duration = sum([i["duration"] for i in deliverables]) # 16.009735 Seconds

.. important:: 
    Finally we have to know that result of each step is saved in two places :
        #. **steps_results** which is an instance variable on Builder instance (in this case BurgerBuilder/its childs).
        #. As attributes on the target object being built (in this case the burger)

API Reference
==============

.. automodule:: core.design_patterns.builder
   :members: