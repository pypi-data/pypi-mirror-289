import pytest
from baserowapi.models.field import LookupField


# Lookup Field Tests
def test_lookupfield_properties_not_none(baserow_client, test_table):
    lookup_field = next(
        (field for field in test_table.fields if field.name == "Lookup"), None
    )
    assert lookup_field is not None
    assert isinstance(lookup_field, LookupField)

    assert lookup_field.through_field_id is not None
    assert lookup_field.through_field_name is not None
    assert lookup_field.target_field_id is not None
    assert lookup_field.target_field_name is not None


def test_lookupfield_compatible_filters(baserow_client, test_table):
    lookup_field = next(
        (field for field in test_table.fields if field.name == "Lookup"), None
    )
    assert lookup_field is not None
    assert isinstance(lookup_field, LookupField)

    expected_filters = [
        "has_empty_value",
        "has_not_empty_value",
        "has_value_equal",
        "has_not_value_equal",
        "has_value_contains",
        "has_not_value_contains",
        "has_value_contains_word",
        "has_not_value_contains_word",
        "has_value_length_is_lower_than",
    ]
    assert lookup_field.compatible_filters == expected_filters
