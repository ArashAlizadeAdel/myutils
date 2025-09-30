import pytest

inputs_for_basic_tests = pytest.mark.parametrize(
    "_class", [(pytest.lazy_fixture("_class_simple")),
               (pytest.lazy_fixture("_class_realistic")),
               (pytest.lazy_fixture("_class_with_function")),
               (pytest.lazy_fixture("_class_with_init")),
               (pytest.lazy_fixture("_class_with_property")),
               ]
    )

inputs_test_singleton_basic_functionality = inputs_for_basic_tests

inputs_test_multiple_singleton_functionality = inputs_for_basic_tests

inputs_test_singleton_attrs_can_change_during_duplicate_instantiation = pytest.mark.parametrize(
    "_class", [
               (pytest.lazy_fixture("_class_realistic")),
               (pytest.lazy_fixture("_class_with_init")),
               ]
    )

inputs_test_prototype_basic_functionality = inputs_for_basic_tests

inputs_test_prototype_advanced_functionality = inputs_for_basic_tests

inputs_test_factory_basic_functionality = inputs_for_basic_tests

inputs_test_builder_basic_functionality = inputs_for_basic_tests

inputs_test_adapter_basic_functionality = inputs_for_basic_tests