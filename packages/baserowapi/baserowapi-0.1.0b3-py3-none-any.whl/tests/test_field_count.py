import pytest
from baserowapi.models.field import CountField


# Functional Tests for CountField
def test_countfield_initialization(baserow_client, test_table):
    count_field = next(
        (field for field in test_table.fields if field.name == "Count"), None
    )
    assert count_field is not None
    assert isinstance(count_field, CountField)
    assert count_field.name == "Count"


def test_countfield_table_id_not_none(baserow_client, test_table):
    count_field = next(
        (field for field in test_table.fields if field.name == "Count"), None
    )
    assert count_field is not None
    assert isinstance(count_field, CountField)
    assert count_field.table_id is not None


def test_countfield_through_field_id_not_none(baserow_client, test_table):
    count_field = next(
        (field for field in test_table.fields if field.name == "Count"), None
    )
    assert count_field is not None
    assert isinstance(count_field, CountField)
    assert count_field.through_field_id is not None


def test_countfield_read_only(baserow_client, test_table):
    count_field = next(
        (field for field in test_table.fields if field.name == "Count"), None
    )
    assert count_field is not None
    assert isinstance(count_field, CountField)
    assert count_field.is_read_only is True


def test_countfield_compatible_filters(baserow_client, test_table):
    count_field = next(
        (field for field in test_table.fields if field.name == "Count"), None
    )
    assert count_field is not None
    assert isinstance(count_field, CountField)

    expected_filters = [
        "equal",
        "not_equal",
        "contains",
        "contains_not",
        "higher_than",
        "lower_than",
        "is_even_and_whole",
        "empty",
        "not_empty",
    ]
    assert count_field.compatible_filters == expected_filters
