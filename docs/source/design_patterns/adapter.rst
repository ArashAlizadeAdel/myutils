===================================
adapter
===================================

Adapter is a design pattern that allows objects with incompatible interfaces to work together. It acts as a bridge between two incompatible classes, converting the interface of one class into another interface that a client expects. Defining such an adapter has the following benefits:

* It promotes reusability by allowing existing classes to be integrated without modifying their source code.
* It enables flexibility, letting you swap or extend adapters at runtime.
* It helps in integrating legacy systems or third-party libraries with new code.

There are two main variations of the adapter pattern: **Object Adapter** (which uses composition) and **Class Adapter** (which uses inheritance). The implementation we provide here is inspired by **Object Adapter**, using composition to wrap and delegate to the adapted object.

How it works
==============

Imagine you're traveling internationally and need to plug your European laptop charger into a US wall socket. The plugs are incompatible, so you use an adapter that converts the European plug to fit the US socket. Similarly, in code, the Adapter helps incompatible classes "fit" together. We'll demonstrate this with a bird analogy: Ducks quack, but Turkeys gobble. We'll adapt a Turkey to behave like a Duck (by making its gobble sound like a quack) so it can join a flock of ducks seamlessly.

#. Import the Adapter class from the package.

    .. code-block:: python

        from core.design_patterns.adapter import Adapter

#. Create some classes with incompatible interfaces. For example, a ``Duck`` class with a ``quack`` method, and a ``Turkey`` class with a ``gobble`` method (which is incompatible if we want it to act like a duck).

    .. code-block:: python

        class Duck:
            def quack(self):
                return "Quack! Quack!"

        class Turkey:
            def gobble(self):
                return "Gobble gobble!"

#. To make the Turkey compatible with code expecting a Duck (i.e., something that can ``quack``), create a ``TurkeyAdapter`` that inherits from ``Adapter``. In the adapter, we'll add a ``quack`` method that translates the ``gobble`` into a duck-like sound (e.g., by calling gobble multiple times to mimic a quack). Pass the Turkey class to the adapter.

    .. code-block:: python

        class TurkeyAdapter(Adapter):
            def quack(self):
                # Adapt gobble to sound like a quack (e.g., gobble three times)
                return self.gobble() + " " + self.gobble() + " " + self.gobble()

        # Create an instance of the adapter wrapping a Turkey
        adapted_turkey = TurkeyAdapter(Turkey)

#. Now, the ``adapted_turkey`` can be used wherever a Duck is expected. It provides the ``quack`` interface, even though the underlying Turkey only knows how to ``gobble``.

    .. code-block:: python

        print(adapted_turkey.quack())  # Gobble gobble! Gobble gobble! Gobble gobble!

        # Example usage in a function expecting a Duck-like object
        def make_bird_sound(bird):
            return bird.quack()

        print(make_bird_sound(adapted_turkey))  # Works! Outputs adapted gobble as quack

#. There may be cases where the adapted object requires initialization parameters. Pass them as kwargs to the Adapter, and it will filter and forward only the relevant ones based on the object's signature.

    .. code-block:: python

        class WildTurkey:
            def __init__(self, name):
                self.name = name

            def gobble(self):
                return f"{self.name} says: Gobble gobble!"

        class WildTurkeyAdapter(Adapter):
            def quack(self):
                return self.gobble().replace("Gobble", "Quack")  # Simple adaptation

        adapted_wild_turkey = WildTurkeyAdapter(WildTurkey, name="Tom")
        print(adapted_wild_turkey.quack())  # Tom says: Quack quack!

#. The Adapter uses dynamic delegation via :meth:`~core.design_patterns.adapter.Adapter.__getattr__`, so you can access any attributes or methods of the wrapped instance directly. If needed, override or add methods in your subclass to perform the actual interface translation.

    .. note::
        The Adapter is abstract (inherits from ABC), but you can subclass it to create specific adapters. This promotes composition over inheritance, making your code more flexible.

.. hint::
    It's recommended to use adapters for classes with similar purposes but different interfaces (e.g., different birds in a flock). This way, you can write more dynamic code that treats adapted objects uniformly, benefiting from polymorphism.

API Reference
==============

.. automodule:: core.design_patterns.adapter
   :members:
   :private-members:
