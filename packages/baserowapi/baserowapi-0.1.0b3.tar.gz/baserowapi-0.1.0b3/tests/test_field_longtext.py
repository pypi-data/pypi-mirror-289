import pytest
from baserowapi.models.field import LongTextField


# Initialization Tests
def test_longtextfield_initialization():
    field_data = {"text_default": "default text"}
    long_text_field = LongTextField(name="Test LongText Field", field_data=field_data)
    assert long_text_field.text_default == "default text"


def test_longtextfield_initialization_invalid_data():
    field_data = {"text_default": 123}  # Invalid type for text_default
    with pytest.raises(ValueError):
        LongTextField(name="Test LongText Field", field_data=field_data)


# CRUD Operation Tests
def test_create_long_text_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Create", "Notes": "Creating a row", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None
    assert added_row["Notes"] == "Creating a row"


def test_read_long_text_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Read", "Notes": "Reading a row", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    rows = list(test_table.get_rows())
    assert len(rows) > 0
    row_id = rows[-1].id
    row = test_table.get_row(row_id)
    assert row is not None
    assert row["Notes"] == "Reading a row"


def test_update_long_text_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Update", "Notes": "Updating a row", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    updated_data = {"Notes": "Updated Notes"}
    updated_rows = test_table.update_rows([{"id": row_id, **updated_data}])
    assert updated_rows[0]["Notes"] == "Updated Notes"


def test_delete_long_text_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Delete", "Notes": "Deleting a row", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    status_code = test_table.delete_rows([row_id])
    assert status_code is True

    rows = list(test_table.get_rows())
    assert not any(row.id == row_id for row in rows)


# Compatibility Tests
def test_longtextfield_compatible_filters():
    field_data = {"text_default": "default text"}
    long_text_field = LongTextField(name="Test LongText Field", field_data=field_data)
    expected_filters = [
        "equal",
        "not_equal",
        "contains",
        "contains_not",
        "contains_word",
        "doesnt_contain_word",
        "length_is_lower_than",
        "empty",
        "not_empty",
    ]
    assert long_text_field.compatible_filters == expected_filters
