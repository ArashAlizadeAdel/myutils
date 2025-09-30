import pytest
import inspect
from core.design_patterns.adapter import Adapter


from .conftest import (inputs_test_adapter_basic_functionality,)

pytestmark = [pytest.mark.design_pattern,
              pytest.mark.unit]


@inputs_test_adapter_basic_functionality
def test_adapter_can_be_initialized(_class):
    '''Initialization with a class and relevant kwargs'''
    
    class TestAdapter(Adapter):
        
        def new_interface(self):
            return self.instance
        
    adapter = TestAdapter(_class, val1=42)
    
    assert isinstance(adapter.new_interface(),_class)
    assert isinstance(adapter.instance,_class)
    
    if hasattr(_class,"val1") :
        assert set(adapter.params) == {"val1"}
        assert adapter.instance.val1 == 42
    
    if hasattr(_class,"x") :
        assert adapter.x
        
@inputs_test_adapter_basic_functionality
def test_initialization_filters_kwargs(_class):
    '''Initialization filters out irrelevant kwargs'''
    
    class TestAdapter(Adapter):
        
        def new_interface(self):
            return self.instance
        
    adapter = TestAdapter(_class, val1=42, irrelevant="ignored")
    
    assert not hasattr(adapter.instance, "irrelevant")

@inputs_test_adapter_basic_functionality
def test_initialization_no_kwargs(_class):
    '''Initialization with no kwargs (uses defaults)'''
    
    class TestAdapter(Adapter):
        
        def new_interface(self):
            return self.instance
    
    if len(inspect.signature(_class).parameters.keys()) == 0 :    
        adapter = TestAdapter(_class)
    
        assert isinstance(adapter.new_interface(),_class)
        assert isinstance(adapter.instance,_class)
        assert set(adapter.params) == set()

def test_adapter_subclass_with_logic():
    '''Subclassing with custom adaptation logic (full adapter example)'''
    # Adaptee: SquarePeg (incompatible with RoundHole)
    class SquarePeg:
        def __init__(self, width):
            self.width = width

        def get_width(self):
            return self.width

    # Target interface: RoundPeg (expected by RoundHole)
    class RoundPeg:
        def __init__(self, radius):
            self.radius = radius

        def get_radius(self):
            return self.radius

    # Adapter: Makes SquarePeg fit like a RoundPeg
    class SquareToRoundAdapter(Adapter):
        def get_radius(self):
            # Adapt: Radius is width / sqrt(2) to fit the square into a circle
            import math
            return self.get_width() / math.sqrt(2)  # Custom adaptation

    # Usage in test
    adapter = SquareToRoundAdapter(SquarePeg, width=10)
    assert adapter.get_width() == 10  # Delegated via __getattr__
    assert round(adapter.get_radius(), 2) == 7.07  # Adapted method

    # Simulate usage: A "hole" that expects RoundPeg
    def fits_in_hole(peg):
        return peg.get_radius() <= 8  # Hole radius of 8

    assert fits_in_hole(adapter)  # True, after adaptation
