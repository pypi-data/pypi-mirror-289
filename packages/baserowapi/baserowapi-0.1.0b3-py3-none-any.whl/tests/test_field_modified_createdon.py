import pytest
import time
from baserowapi.models.field import LastModifiedField, CreatedOnField
from baserowapi.models.row_value import LastModifiedRowValue, CreatedOnRowValue


# Initialization Tests
def test_lastmodifiedfield_initialization():
    field_data = {
        "id": 1358466,
        "table_id": 198958,
        "name": "Last modified",
        "order": 6,
        "type": "last_modified",
        "primary": False,
        "read_only": True,
        "description": None,
        "date_format": "US",
        "date_include_time": False,
        "date_time_format": "24",
        "date_show_tzinfo": True,
        "date_force_timezone": None,
    }
    last_modified_field = LastModifiedField(
        name="Test Last Modified Field", field_data=field_data
    )
    assert last_modified_field.name == "Test Last Modified Field"
    assert last_modified_field.is_read_only is True


def test_createdonfield_initialization():
    field_data = {
        "id": 1358467,
        "table_id": 198958,
        "name": "Created on",
        "order": 7,
        "type": "created_on",
        "primary": False,
        "read_only": True,
        "description": None,
        "date_format": "US",
        "date_include_time": True,
        "date_time_format": "24",
        "date_show_tzinfo": False,
        "date_force_timezone": None,
    }
    created_on_field = CreatedOnField(
        name="Test Created On Field", field_data=field_data
    )
    assert created_on_field.name == "Test Created On Field"
    assert created_on_field.is_read_only is True


# Row Value Tests
def test_lastmodifiedrowvalue_set_value_error():
    field_data = {
        "id": 1358466,
        "table_id": 198958,
        "name": "Last modified",
        "order": 6,
        "type": "last_modified",
        "primary": False,
        "read_only": True,
        "description": None,
        "date_format": "US",
        "date_include_time": False,
        "date_time_format": "24",
        "date_show_tzinfo": True,
        "date_force_timezone": None,
    }
    last_modified_field = LastModifiedField(
        name="Test Last Modified Field", field_data=field_data
    )
    last_modified_row_value = LastModifiedRowValue(
        field=last_modified_field, raw_value="2024-08-05"
    )

    with pytest.raises(
        ValueError, match="Cannot set value for a read-only LastModifiedRowValue."
    ):
        last_modified_row_value.value = "2024-08-06"


def test_createdonrowvalue_set_value_error():
    field_data = {
        "id": 1358467,
        "table_id": 198958,
        "name": "Created on",
        "order": 7,
        "type": "created_on",
        "primary": False,
        "read_only": True,
        "description": None,
        "date_format": "US",
        "date_include_time": True,
        "date_time_format": "24",
        "date_show_tzinfo": False,
        "date_force_timezone": None,
    }
    created_on_field = CreatedOnField(
        name="Test Created On Field", field_data=field_data
    )
    created_on_row_value = CreatedOnRowValue(
        field=created_on_field, raw_value="2024-08-05T14:00:00Z"
    )

    with pytest.raises(
        ValueError, match="Cannot set value for a read-only CreatedOnRowValue."
    ):
        created_on_row_value.value = "2024-08-06T14:00:00Z"


# CRUD Operation Tests (Read-only fields should only be tested for reading, not creation, updating, or deletion)
def test_read_last_modified_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Read", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    rows = list(test_table.get_rows())
    assert len(rows) > 0
    row_id = rows[-1].id
    row = test_table.get_row(row_id)
    assert row is not None

    retries = 5
    for _ in range(retries):
        if "Last modified" in row.content:
            break
        time.sleep(1)
        row = test_table.get_row(row_id)

    assert "Last modified" in row.content
    assert isinstance(row.content["Last modified"], str)


def test_read_created_on_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Read", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    rows = list(test_table.get_rows())
    assert len(rows) > 0
    row_id = rows[-1].id
    row = test_table.get_row(row_id)
    assert row is not None

    retries = 5
    for _ in range(retries):
        if "Created on" in row.content:
            break
        time.sleep(1)
        row = test_table.get_row(row_id)

    assert "Created on" in row.content
    assert isinstance(row.content["Created on"], str)
