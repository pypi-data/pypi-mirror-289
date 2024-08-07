import pytest
from baserowapi.models.field import NumberField


# Initialization Tests
def test_numberfield_initialization():
    field_data = {
        "id": 1358461,
        "table_id": 198958,
        "name": "Number",
        "order": 3,
        "type": "number",
        "primary": False,
        "read_only": False,
        "description": None,
        "number_decimal_places": 2,
        "number_negative": True,
    }
    number_field = NumberField(name="Test Number Field", field_data=field_data)
    assert number_field.name == "Test Number Field"
    assert number_field.number_decimal_places == 2
    assert number_field.number_negative is True


# CRUD Operation Tests
def test_create_number_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Create", "Number": "123.45", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None
    assert added_row["Number"] == "123.45"


def test_read_number_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Read", "Number": "123.45", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    rows = list(test_table.get_rows())
    assert len(rows) > 0
    row_id = rows[-1].id
    row = test_table.get_row(row_id)
    assert row is not None
    assert row["Number"] == "123.45"


def test_update_number_field_with_string(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Update", "Number": "123.45", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    updated_data = {"Number": "543.21"}  # String representation of a number
    updated_rows = test_table.update_rows([{"id": row_id, **updated_data}])
    assert updated_rows[0]["Number"] == "543.21"  # Ensure it matches the string format


def test_update_number_field_with_float(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Update", "Number": "123.45", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    updated_data = {"Number": 543.21}  # Float value
    updated_rows = test_table.update_rows([{"id": row_id, **updated_data}])
    assert updated_rows[0]["Number"] == "543.21"  # Ensure it matches the string format


def test_delete_number_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Delete", "Number": "123.45", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    status_code = test_table.delete_rows([row_id])
    assert status_code is True

    rows = list(test_table.get_rows())
    assert not any(row.id == row_id for row in rows)


# Compatibility Tests
def test_numberfield_compatible_filters():
    field_data = {
        "id": 1358461,
        "table_id": 198958,
        "name": "Number",
        "order": 3,
        "type": "number",
        "primary": False,
        "read_only": False,
        "description": None,
        "number_decimal_places": 2,
        "number_negative": True,
    }
    number_field = NumberField(name="Test Number Field", field_data=field_data)
    expected_filters = [
        "equal",
        "not_equal",
        "contains",
        "contains_not",
        "higher_than",
        "higher_than_or_equal",
        "lower_than",
        "lower_than_or_equal",
        "is_even_and_whole",
        "empty",
        "not_empty",
    ]
    assert number_field.compatible_filters == expected_filters
