import pytest
from tests.conftest import (_class_simple,
                            _class_realistic,
                            _class_with_function,
                            _class_with_init,
                            _class_with_property)


inputs_test_singleton_basic_functionality = pytest.mark.parametrize(
    "_class", [(pytest.lazy_fixture("_class_simple")),
               (pytest.lazy_fixture("_class_realistic")),
               (pytest.lazy_fixture("_class_with_function")),
               (pytest.lazy_fixture("_class_with_init")),
               (pytest.lazy_fixture("_class_with_property")),
               ]
    )

inputs_test_multiple_singleton_functionality = pytest.mark.parametrize(
    "_class", [(pytest.lazy_fixture("_class_simple")),
               (pytest.lazy_fixture("_class_realistic")),
               (pytest.lazy_fixture("_class_with_function")),
               (pytest.lazy_fixture("_class_with_init")),
               (pytest.lazy_fixture("_class_with_property")),
               ]
    )

inputs_test_singleton_attrs_can_change_during_duplicate_instantiation = pytest.mark.parametrize(
    "_class", [
               (pytest.lazy_fixture("_class_realistic")),
               (pytest.lazy_fixture("_class_with_init")),
               ]
    )