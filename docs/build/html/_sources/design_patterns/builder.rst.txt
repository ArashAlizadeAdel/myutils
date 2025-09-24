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


API Reference
==============

.. automodule:: core.design_patterns.builder
   :members: