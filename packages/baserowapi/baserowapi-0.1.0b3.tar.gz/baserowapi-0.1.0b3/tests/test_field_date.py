import pytest
from baserowapi.models.field import DateField
from datetime import datetime


# Initialization Tests
def test_datefield_initialization():
    field_data = {
        "id": 1392711,
        "table_id": 198958,
        "name": "EU Date",
        "order": 20,
        "type": "date",
        "primary": False,
        "read_only": False,
        "description": None,
        "date_format": "EU",
        "date_include_time": False,
        "date_time_format": "24",
        "date_show_tzinfo": False,
        "date_force_timezone": None,
    }
    date_field = DateField(name="Test EU Date Field", field_data=field_data)
    assert date_field.name == "Test EU Date Field"
    assert date_field.date_format == "EU"
    assert date_field.date_include_time is False
    assert date_field.date_time_format == "24"
    assert date_field.date_show_tzinfo is False


# CRUD Operation Tests
def test_create_date_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Create", "EU Date": "2024-01-01", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None
    assert added_row["EU Date"] == "2024-01-01"


def test_read_date_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Read", "EU Date": "2024-01-01", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    rows = list(test_table.get_rows())
    assert len(rows) > 0
    row_id = rows[-1].id
    row = test_table.get_row(row_id)
    assert row is not None
    assert row["EU Date"] == "2024-01-01"


def test_update_date_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Update", "EU Date": "2024-01-01", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    updated_data = {"EU Date": "2025-02-02"}
    updated_rows = test_table.update_rows([{"id": row_id, **updated_data}])
    assert updated_rows[0]["EU Date"] == "2025-02-02"


def test_delete_date_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Delete", "EU Date": "2024-01-01", "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    status_code = test_table.delete_rows([row_id])
    assert status_code is True

    rows = list(test_table.get_rows())
    assert not any(row.id == row_id for row in rows)


# Compatibility Tests
def test_datefield_compatible_filters():
    field_data = {
        "id": 1392711,
        "table_id": 198958,
        "name": "EU Date",
        "order": 20,
        "type": "date",
        "primary": False,
        "read_only": False,
        "description": None,
        "date_format": "EU",
        "date_include_time": False,
        "date_time_format": "24",
        "date_show_tzinfo": False,
        "date_force_timezone": None,
    }
    date_field = DateField(name="Test EU Date Field", field_data=field_data)
    expected_filters = [
        "date_equal",
        "date_not_equal",
        "date_equals_today",
        "date_before_today",
        "date_after_today",
        "date_within_days",
        "date_within_weeks",
        "date_within_months",
        "date_equals_days_ago",
        "date_equals_months_ago",
        "date_equals_years_ago",
        "date_equals_week",
        "date_equals_month",
        "date_equals_year",
        "date_equals_day_of_month",
        "date_before",
        "date_before_or_equal",
        "date_after",
        "date_after_or_equal",
        "date_after_days_ago",
        "contains",
        "contains_not",
        "empty",
        "not_empty",
    ]
    assert date_field.compatible_filters == expected_filters


# Validation Tests
def test_validate_value_us_date_time():
    field_data = {
        "id": 1358464,
        "table_id": 198958,
        "name": "US Date Time",
        "order": 5,
        "type": "date",
        "primary": False,
        "read_only": False,
        "description": None,
        "date_format": "US",
        "date_include_time": True,
        "date_time_format": "24",
        "date_show_tzinfo": True,
        "date_force_timezone": None,
    }
    date_field = DateField(name="Test US Date Time Field", field_data=field_data)

    # Valid values
    date_field.validate_value("2024-01-01T12:34:56Z")
    date_field.validate_value("2024-01-01T12:34:56+00:00")

    # Invalid values
    with pytest.raises(ValueError):
        date_field.validate_value("2024-01-01")

    with pytest.raises(ValueError):
        date_field.validate_value("01-01-2024T12:34:56Z")


def test_validate_value_eu_date():
    field_data = {
        "id": 1392711,
        "table_id": 198958,
        "name": "EU Date",
        "order": 20,
        "type": "date",
        "primary": False,
        "read_only": False,
        "description": None,
        "date_format": "EU",
        "date_include_time": False,
        "date_time_format": "24",
        "date_show_tzinfo": False,
        "date_force_timezone": None,
    }
    date_field = DateField(name="Test EU Date Field", field_data=field_data)

    # Valid value without time
    date_field.validate_value("2024-01-01")

    # Invalid value with time
    with pytest.raises(ValueError):
        date_field.validate_value("2024-01-01T12:34:56Z")


def test_validate_value_empty_date():
    field_data = {
        "id": 1392711,
        "table_id": 198958,
        "name": "EU Date",
        "order": 20,
        "type": "date",
        "primary": False,
        "read_only": False,
        "description": None,
        "date_format": "EU",
        "date_include_time": False,
        "date_time_format": "24",
        "date_show_tzinfo": False,
        "date_force_timezone": None,
    }
    date_field = DateField(name="Test EU Date Field", field_data=field_data)

    # Empty value should be valid
    date_field.validate_value(None)

    # Empty string should be invalid
    with pytest.raises(ValueError):
        date_field.validate_value("")


def test_validate_value_invalid_date_format():
    field_data = {
        "id": 1358464,
        "table_id": 198958,
        "name": "US Date Time",
        "order": 5,
        "type": "date",
        "primary": False,
        "read_only": False,
        "description": None,
        "date_format": "US",
        "date_include_time": True,
        "date_time_format": "24",
        "date_show_tzinfo": True,
        "date_force_timezone": None,
    }
    date_field = DateField(name="Test US Date Time Field", field_data=field_data)

    # Invalid date format
    with pytest.raises(ValueError):
        date_field.validate_value("2024/01/01T12:34:56Z")

    with pytest.raises(ValueError):
        date_field.validate_value("2024-13-01T12:34:56Z")
