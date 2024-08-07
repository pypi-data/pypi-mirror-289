import pytest
from baserowapi.models.field import BooleanField


# Initialization Tests
def test_booleanfield_initialization():
    field_data = {
        "id": 1358460,
        "table_id": 198958,
        "name": "Active",
        "order": 2,
        "type": "boolean",
        "primary": False,
        "read_only": False,
        "description": None,
    }
    boolean_field = BooleanField(name="Test Boolean Field", field_data=field_data)
    assert boolean_field.name == "Test Boolean Field"


# CRUD Operation Tests
def test_create_boolean_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Create", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None
    assert added_row["Active"] is True


def test_read_boolean_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Read", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    rows = list(test_table.get_rows())
    assert len(rows) > 0
    row_id = rows[-1].id
    row = test_table.get_row(row_id)
    assert row is not None
    assert row["Active"] is True


def test_update_boolean_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Update", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    updated_data = {"Active": False}
    updated_rows = test_table.update_rows([{"id": row_id, **updated_data}])
    assert updated_rows[0]["Active"] is False


def test_delete_boolean_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Delete", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    status_code = test_table.delete_rows([row_id])
    assert status_code is True

    rows = list(test_table.get_rows())
    assert not any(row.id == row_id for row in rows)


# Compatibility Tests
def test_booleanfield_compatible_filters():
    field_data = {
        "id": 1358460,
        "table_id": 198958,
        "name": "Active",
        "order": 2,
        "type": "boolean",
        "primary": False,
        "read_only": False,
        "description": None,
    }
    boolean_field = BooleanField(name="Test Boolean Field", field_data=field_data)
    expected_filters = [
        "boolean",
        "empty",
        "not_empty",
    ]
    assert boolean_field.compatible_filters == expected_filters
