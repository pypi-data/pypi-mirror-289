import pytest
from baserowapi.models.field import TextField


# Initialization Tests
def test_textfield_initialization():
    field_data = {"text_default": "default text"}
    text_field = TextField(name="Test Field", field_data=field_data)
    assert text_field.text_default == "default text"


def test_textfield_initialization_invalid_default():
    field_data = {"text_default": 123}  # Invalid type
    with pytest.raises(ValueError):
        TextField(name="Test Field", field_data=field_data)


# CRUD Operation Tests
def test_create_text_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Create", "Notes": "Creating a row", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None
    assert added_row["Name"] == "Test Create"


def test_read_text_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Read", "Notes": "Reading a row", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    rows = list(test_table.get_rows())
    assert len(rows) > 0
    row_id = rows[-1].id
    row = test_table.get_row(row_id)
    assert row is not None
    assert row["Name"] == "Test Read"


def test_update_text_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Update", "Notes": "Updating a row", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    updated_data = {"Name": "Updated Name"}
    updated_rows = test_table.update_rows([{"id": row_id, **updated_data}])
    assert updated_rows[0]["Name"] == "Updated Name"


def test_delete_text_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Delete", "Notes": "Deleting a row", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    status_code = test_table.delete_rows([row_id])
    assert status_code is True

    rows = list(test_table.get_rows())
    assert not any(row.id == row_id for row in rows)


# Compatibility Tests
def test_textfield_compatible_filters():
    field_data = {"text_default": "default text"}
    text_field = TextField(name="Test Field", field_data=field_data)
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
    assert text_field.compatible_filters == expected_filters
