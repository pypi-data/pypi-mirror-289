import pytest
from baserowapi.models.field import SingleSelectField, MultipleSelectField


# CRUD Operation Tests
def test_create_single_select_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Create", "SingleSelect": "option 1", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None
    assert added_row["SingleSelect"] == "option 1"


def test_read_single_select_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Read", "SingleSelect": "option 1", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    rows = list(test_table.get_rows())
    assert len(rows) > 0
    row_id = rows[-1].id
    row = test_table.get_row(row_id)
    assert row is not None
    assert row["SingleSelect"] == "option 1"


def test_update_single_select_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Update", "SingleSelect": "option 1", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    updated_data = {"SingleSelect": "option 2"}
    updated_rows = test_table.update_rows([{"id": row_id, **updated_data}])
    assert updated_rows[0]["SingleSelect"] == "option 2"


def test_delete_single_select_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Delete", "SingleSelect": "option 1", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    status_code = test_table.delete_rows([row_id])
    assert status_code is True

    rows = list(test_table.get_rows())
    assert not any(row.id == row_id for row in rows)


def test_create_multiple_select_field(baserow_client, test_table, test_row_manager):
    new_row_data = {
        "Name": "Test Create",
        "MultipleSelect": ["option 1", "option 2"],
        "Active": True,
    }
    added_row = test_row_manager(new_row_data)
    assert added_row is not None
    assert set(added_row["MultipleSelect"]) == {"option 1", "option 2"}


def test_read_multiple_select_field(baserow_client, test_table, test_row_manager):
    new_row_data = {
        "Name": "Test Read",
        "MultipleSelect": ["option 1", "option 2"],
        "Active": True,
    }
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    rows = list(test_table.get_rows())
    assert len(rows) > 0
    row_id = rows[-1].id
    row = test_table.get_row(row_id)
    assert row is not None
    assert set(row["MultipleSelect"]) == {"option 1", "option 2"}


def test_update_multiple_select_field(baserow_client, test_table, test_row_manager):
    new_row_data = {
        "Name": "Test Update",
        "MultipleSelect": ["option 1", "option 2"],
        "Active": True,
    }
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    updated_data = {"MultipleSelect": ["option 1"]}
    updated_rows = test_table.update_rows([{"id": row_id, **updated_data}])
    assert set(updated_rows[0]["MultipleSelect"]) == {"option 1"}


def test_delete_multiple_select_field(baserow_client, test_table, test_row_manager):
    new_row_data = {
        "Name": "Test Delete",
        "MultipleSelect": ["option 1", "option 2"],
        "Active": True,
    }
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    status_code = test_table.delete_rows([row_id])
    assert status_code is True

    rows = list(test_table.get_rows())
    assert not any(row.id == row_id for row in rows)


# Tests for field options
def test_single_select_field_options(test_table):
    single_select_field = test_table.fields["SingleSelect"]
    assert isinstance(single_select_field.options, list)
    assert len(single_select_field.options) > 0
    assert isinstance(single_select_field.options_details, list)
    assert len(single_select_field.options_details) > 0


def test_multiple_select_field_options(test_table):
    multiple_select_field = test_table.fields["MultipleSelect"]
    assert isinstance(multiple_select_field.options, list)
    assert len(multiple_select_field.options) > 0
    assert isinstance(multiple_select_field.options_details, list)
    assert len(multiple_select_field.options_details) > 0
